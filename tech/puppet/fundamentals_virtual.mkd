# Puppet Virtual Fundamentals


https://drive.google.com/drive/folders/0BwjXv3TJiWYESDhLTVd6U2xGMDQ

## About Puppet

- Identify the challenges of infrastructure management.
- Explain how Puppet Enterprise can be used to overcome such challenges.
- Describe Puppet's approach to configuration management.

Model Based Approach
- Describe
- Simulate
- Enforce
- Report

## Classroom Environment

### Agenda

- Have a classroom account for testing Puppet code.
- Be able to use facter to display information about a node.
- Be able to use puppet resource to inspect local resources.

### Facter

`facter` is a system inventory tool

Output can be used in puppet manifests e.g.

```puppet
case $os['release']['major'] {
  ' 7' : { include myapp:: init:: systemd }
  ' 6' : { include myapp:: init:: sysvinit }
  default: { fail( 'Unsupported OS major version' ) }
}
```

`facter os.release.major`

### $ puppet resource

`puppet resource user` return all users

`puppet resource user elvis` return user elvis

### Puppet Component Roles

- Describe the roles of the Agent and the Master.
- Classify a node with desired configurations.
- Use the reporting features of the Puppet Enterprise console.
- Run the Puppet Agent from the command line.

Puppet Infrastructure
- Puppet Master
- PE Console
- PuppetDB
- Compile Masters
- Puppet CA

### Puppet Master

is responsible for:
- Authenticating agent connections.
- Signing certificates.
- Serving a compiled catalog to the agent.
- Serving files.
- Processing posted reports.
- Supports several Linux distributions.
- Runs under JRuby on the JVM for increased performance at scale.

### $ puppet agent

```puppet agent
  --test
    --no-daemonize
    --verbose
    --onetime

  --noop
  --debug
  --environment <env>
  --configprint <config option>
```

### PE Configuration: /etc/puppetlabs/puppet/puppet.conf

```
[main]
  certname = master. puppetlabs. vm
  server = master. puppetlabs. vm
  user = pe-puppet
  group = pe-puppet
  archive_files = true
  archive_file_server = master. puppetlabs. vm
  app_management = true
  module_groups = base+pe_only
  environmentpath = /etc/puppetlabs/code/environments
  disable_warnings=deprecations

[agent]
  graph = true
  environment_timeout=0

[master]
  node_terminus = classifier
  storeconfigs = true
  storeconfigs_backend = puppetdb
  reports = puppetdb
  certname = master. puppetlabs. vm
  always_cache_features = true
```

Each `[section]` corresponds to a **run mode**

Settings order is `command line > run mode > [main] > puppet defaults`
- i.e. setting in `[agent]` will override `[main]`

### Puppet modulepath

`puppet apply --configprint modulepath` to see where modules are pulled from 
when using `puppet apply`

`puppet master --configprint modulepath --environment development` to see where 
the master pulls modules from when running in `development` environment

Other interesting variables:
- `vardir` location where Puppet stores dynamically growing information.
- `rundir` location where Puppet PID files are stored.
- `ssldir` location where SSL certificates are stored.
- `ca_server` the server to use for certificate authority requests.
- `cerrtname` the certificate name to use when communicating with the master.
- `server` the host name of the puppetmaster.

### Agent/Master Architecture

    Puppet Master       |File|  |Manifests|   |Templates|
    ---------------------------------------------------
                          |                       ^
                          |                       |
                        Catalog     |SSL|       Facts
                          |                       |
                          v                       |
    ---------------------------------------------------
    Puppet Agent        RAL         |
                     -------------- | Facter
                    Resource Types  |
                                    |
                              Operating System Calls

- Agent sends *facts* to master
- Master returns *catalog* to agent

### PE Console

GUI for puppet
- Presenting an overview of your systems.
- Providing detailed information about each node.
- Collating and displaying statistics.
- Providing an interface for node classification.
- Enabling report browsing and viewing.

- `Nodes -> Inventory` for node details and statistics
- `Nodes -> Classification` to set **node groups**
- `Configuration -> Reports` for latest reports
- `Configuration -> Events` for latest events

### Exercise 4.1: Explore the PE Console

## Basic Puppet Concepts

### Checkpoint: Component Roles

What do the parts of Puppet Enterprise do?

The Puppet Agent compiles a catalog.
- True
- ✓ False

What information does the Master have about the Agent?
- ✓ Facts gathered by the agent
- ✓ The list of packages installed on the agent
- ✓ Home directories of non-system users
- ✓ A list of the providers on the agent

The machine running the Puppet Master typically also runs the Agent.
- ✓ True
- False

The Puppet Enterprise Console allows the user to:
- ✓ Define rules to classify nodes
- ✓ See which nodes are currently applying a catalog
- ✓ See a quick overview of your infrastructure
- ✓ Browse reports and view results of individual agent runs
- Look busy when the boss walks by

### Puppet Resources

- `Service` e.g. sshd
- `Package` e.g. opensshd
- `File` e.g. sshd_config
- `User`

### $ puppet describe

Use `puppet describe user` to view documentation for the user resource

Resources in Puppet are **abstracted** from the underlying **providers**

e.g. `package { 'postresql': ensure => present, }` equates to
- `yum install postgresql`
- `apt-get install postgresql`

### RAL: Resource Abstraction Layer

Provides consistent resource model across supported platforms
- `File` Posix, Windows
- `Package` Gem, yum, Portage, RPM, Windows
- `Service` Launchd, Systemd, Upstart, Windows
- `User` AIX, HPUX, Useradd, LDAP

File, Package, Service, User == **Types**

POSIX, Windows, etc == **Providers**

`ls /opt/puppetlabs/puppet/lib/ruby/vendor_ruby/puppet/provider/package` to 
view supported providers for `package`

### $ puppet apply

`puppet apply`
- **compiles** a puppet manifest into a resource catalog
- **simulate** or **enforce** the catalog locally

`puppet apply --noop` to simulate

### Checkpoint: Basic Puppet Concepts

What does it mean to manage configuration state?

Running the Puppet Agent multiple times is a safe operation.
- ✓ True
- False

Configuration drift only occurs when unauthorized manual changes take place.
- ✓ True
- False

Combining resources into larger components often leads to dependency errors.
- True
- ✓ False

What are some of ways that the Puppet language is readable?
- Utility methods are provided to check command exit codes
- ✓ All resource types are interacted with in very similar ways
- ✓ Most resource types can be used on different platforms without modification
- Robust concurrency primitives are provided directly in the language
- ✓ It comes with a glossary you can give to your boss

## Resources

### Objectives:

- Identify several key resource types.
- Describe the purpose of a resource's title and namevar .
- Explain why resources support different features on different platforms.
- Discover new resource types and their attributes.

### Resource Type Listing

`puppet describe --list` will list resource types available. If you can't find 
what you need then you can install from the **forge**

`puppet describe <type> [-s]`
- `-s` provides summary only

e.g. `puppet describe user -s` to view doc for resource type User

Default resources come with puppet or they may come from **modules** 

**Providers are limited to funcationality exposed by the OS**. e.g.  only the 
Solaris `user_role_add` is able to manage Solaris user roles

### title vs namevar

```puppet
package { 'ssh':
  ensure => present,
  name   => 'openssh-clients',
}
```

The **title** is 'ssh'.
- used by puppet to identify the resource internally e.g. `Package['ssh']`

The `namevar` is 'openssh-clients'
- the name of the package as the package manager sees it

`namevar` will vary by resource. e.g.
- `package` => `name`
- `file` => `path`

`namevar` can be omitted and will **default** to the `title`

### meta resource types

- `notify`
- `resources`
- `schedule`
- `exec`

## Modules and Classes

### Objective
- Describe the structure of, build, and use a basic Puppet module.
- Describe the benefits of using a module to contain configuration.
- Explain how modules allow Puppet to auto-load content.
- Differentiate between defining and declaring classes.

### Puppet Classes

**class** bundles other resources

```puppet
class ssh {
  package { 'openssh':
    ...
  }
  file { '/etc/ssh/sshd_config':
    ...
  }
  service { 'sshd':
    ...
  }
```

### Modules

**module** are **directories** that encapsulate components related to a given 
configuration

They have a **pre-defined** structure that enable:
- **Auto-loading** of classes.
- **File-serving** for templates and files.
- **Auto-delivery** of custom Puppet extensions.
- Easy **sharing** with others.

`puppet master --configprint basemodulepath` to view where modules can be 
located

Naming classes with `::scope` in module structure...

```
tree /etc/puppetlabs/code/environments/production/modules/apache/

- manifests
  - init.pp               ## class apache { ... }
  - mod
    - php.pp              ## class apache::mod::php { ... }
  - mod.pp                ## class apache::mod { ... }
```

### include

`include` can be used to include other classes e.g.

```puppet
class profile::base {
  include ssh
  include ...
}
class profile::hardened {
  include ssh
  include ...
}
```

but the catalog will only include a **single instance** of each class i.e.

```puppet
node 'example.puppetlabs.vm' {
  include profile::base
  include profile::hardened
}
```

Classes have to **unique**

### File Source

We can use `source` to "relatively" link to a file source

```puppet
file { 'etc/sudoers':
  ...
  source => 'puppet://modules/sudo/sudoers',
}
```

`puppet:///[source]/<moundpoint>/<module>/<file path>`
- `[source]` defaults to wherever the catalog came from. Usually left blank.
- `<mountpoint>` of modules instructs Puppet to search the modulepath.
- `<module>` is the name of the module to look for.
- `<file path>` is the path to a filewithin that modules's files directory

```
$ tree /etc/puppetlabs/code/environments/production/modules/sudo/

|- files
   |- sudoers     ## source => 'puppet:///modules/sudo/sudoers',
   |- sudoers.d
      |- admins   ## source => 'puppet:///modules/sudo/sudoers.d/admins',
   |- manifests
      |- init.pp  ## class sudo { ...}
```

## Classification

### Objectives

- Explain the concept of **node classification**.
- Write a **node definition** in your site manifest.
- Use **classification rules** in the Puppet Enterprise Console.
- Assign nodes to **node groups**.

### Nodes

Agent node **certname** is how it is identified by Puppet. The certname is 
*usually* but not always the `fqdn`

Best practice to only `include` in a node definition

```puppet
node 'food.puppet.com' {
  include ssh
  include ...
}
```

Can use regex in nodename

```puppet
node /^web\d{3}\.puppetlabs\.com$/ {
  include ...
}
```

There is also a `node default`

## Resource Relationships

### metaparameters

4 metaparameters to establish relationships
- `require`
- `before`
- `subscribe` similar to require but establishes refresh relationship
- `notify` similar to before but establishes refresh relationship

Some dependencies are implicit e.g. `group` ~> `user`

## Language Constructs

### Variables

e.g. `$httpd_dir = ...`

Can be used as titles `file { $httpd_dir: ... }`

Can be used as attribute values `file { ...: content => $readme_content, }`

### Strings

single-quote does not allow variable interpolation
- `$string = 'string ${mystring}\n'`
- `$string = "string ${mystring}\n"`

Can be assigned at top of class

```puppet
class apache {
  $httpd_dir = '/etc/httpd/conf.d'

  file { $httpd_dir:
    ensure => directory,
  }

  file { "${httpd_dir}/www1.conf":
    content => "Configuring ${httpd_dir}/www1.conf",
  }
```

Variable are **immutable**

### Variable Scope

Must include other class if you want to use it out of scope

```puppet
class apache::params { $logroot = 'var/log/httpd' }

class apache::logs {
  include apache::params   # must include if you want to use its vars

  file { "${logroot}/httpd.log": ... }
}
```

### Facts are global vars

```puppet
"Configuing ${httpd_dir} for ${::hostname}"
```

### $facts Hash

```puppet
"${facts['networking']['hostname']"
```

### Resource defaults

```puppet
class apache {

  File {                  # sets defaults for file resource
    owner => 'root'
  }

  file { ...:
    ensure => file,      # owner also gets set here
  }
}
```

### Resource defaults in site.pp

Can also set global resource defaults e.g. for windows

```puppet
  # <ENVIRONMENTS DIRECTORY>/production/manifests/site.pp
  # top level tweaks for windows

if $facts[' os' ] [' family' ] == ' windows' {

  Package {
    provider => ' chocolatey' , # assigns default provider for windows
  }
}
```

### Arrays

```puppet
$somearray = ['one', 'two' ]        # array var

user { 'elvis':
  groups => ['jailhouse', 'surfer'], # can be passed to resource parameters
}

file { ['/tmp/1', '/tmp/2']:    # in title (will create 2 file resources
  ...
}

service { ...
  require => [ File['1'], File['2'] ], # argument to params
}
```

### Conditional Expressions

- Selectors
- Case
- `if`
- `unless`

#### Selectors

```puppet
name => $facts['os']['name'] ? {
  'ubuntu' => 'ssh',
  ...
  default => 'openssh',
}
```

Selectors **must return a value**

Can also be stored in a var

```puppet
$sshpkgname = $facts['os']['name'] ? {
  'ubuntu' => 'ssh',
  ...
  default => 'openssh',
}
```

#### Case

```puppet
case $facts['os']['name'] {
  'redhat', 'centos': { include redhat }
  'debian', 'ubuntu': { include debian }
  'amazon': {
    include amazon
    include redhat
    notify { "Amazoning" }
  }
  default: { fail("whale") }
}
```

#### Boolean expressions

Everything except for `undef` and `false` is **true**

Conditionals: `if` `elseif` `else` `unless`

Can use `=~` for regex comparisons e.g. `if $s =~ /DBna\d+$/`

- `and , or , and not`
- `== , ! = , =~ , < , > , <= , >=`
- `+ , - , / , * , << , >>`
- `in`

#### Functions

**Statement** functions don't return a value
- `tag` Sets a tag for all resources contained in the current scope.
- `include` Evaluate a class.
- `require` Evaluate one or more classes, adding the required class as a 
  dependency
- `fail` Fail with a parse error.

**rvalue** functions return a value
- `defined` returns true if a class or resource is declared
- `file` returns the contents of a file from the server
- `versioncmp` compares two version number strings
- `regsubst` regex string replacement
- `pick` returns the first argument with a value (stdlib)

```puppet
  # Use $pe_server_version if set, otherwise fall back to $pe_version
$version = pick( $facts['pe_server_version'] , $facts['pe_version'] )

  # if $version is older than 201 5. 2 then fail compilation with a warning
if versioncmp($version, '2015.2.0') < 0 {
  fail("This Training VM is out of date. Please update: ${download_url}")
}
```

## Templates

### EPP vs ERB

File resource templates `<% ... %>`

```puppet
 # mymodule/manifests/init.pp
$somevariable = 'Somevalue'

 # mymodule/tempaltes/mytempalte.epp
$content = epp('mymodule/mytemplate.epp', { myparam => #somevariable })

 # in the template
IP address is <%= $ipaddress %>
```

Also can iterate over arrays/hashes

```puppet
<%# <module>/templates/interfaces.epp -%>
<% $networking['interfaces'].each |$iface, $value| { -%>
  Interface <%= $iface %> has an IP of <%= $value['ip'] %>
<% }
```

### --facts to add variables to epp

```puppet
$ facter --yaml > facts.yaml
$ puppet epp render ec2data.epp --facts facts.yaml
```

### Using epp templates

```puppet
file { ...
  content => epp('apache/httpd.conf.epp'),
}
```

Which is loaded in `<module>/templates`

## Defined Resource Types

### define

`define` to create your own type

```puppet
define apache: : vhost (
  $docroot,
  $port = '80',
  $priority = '10',
  $options = 'Indexes MultiViews',
  $vhost_name = $title,
  $servername = $title,
  $logdir = '/var/log/httpd',
) {
  file { "/etc/httpd/conf.d/${title}.conf":
    ensure => file,
    owner => 'apache',
    group => 'apache',
    mode => '0644',
    content => epp('apache/vhost.conf.epp', {
      'docroot' => $docroot,
      'port' => $port,
      # other parameters used in the template
  }),
  notify => Service['httpd'],
  }
}
```

Can be used as

```puppet
apache::vhost { 'elmo.puppet.com':
  port => '80',
  docroot => '/var/www/muppets/elmo',
  options => 'Indexes MultiViews',
}

apache::vhost { 'piggy.puppet.com':
  port => '80',
  docroot => '/var/www/muppets/piggy',
  options => '-MultiViews',
}
```

Resource title must be **unique**

Should be organized like classes

## Data Separation

### Heira

**Heira** externally set key:values per node or all nodes

/etc/puppetlabs/code/environments/production/hieradata/common.yaml
```puppet
message: "This is a sample variable that came from Hiera"
```

`$ puppet apply -e "notice(heira('message'))"`

### Heira configuration

Heira is **rarely configured on the agent**. Will be available when running 
`puppet apply` on the agent but not when `puppet agent -t` since master doesn't 
have access to agent heira.

Default configuration is at `/etc/puppetlabs/puppet/heira.yaml`

/etc/puppetlabs/puppet/hiera.yaml
```yaml
:backends:
  - yaml

:yaml:
  :datadir: '/etc/puppetlabs/code/environments/production/hieradata'

:hierarchy:
  - "%{::clientcert}"
  - "%{::datacenter}"
  - common
```

### Heira resolution order

Heira by defaults resolves in order:
1. `/etc/puppetlabs/code/environments/production/heiradata/%{clientcert}.yaml`
2. `/etc/puppetlabs/code/environments/production/heiradata/%{datacenter}.yaml`
3. `/etc/puppetlabs/code/environments/production/heiradata/common.yaml`

Can debug with `puppet apply -e 'notice(heira("ntpserver"))' --debug --environment 
development`

So for configuration of `ntpserver` for `node1.example.com` in the `houston` 
datacenter, the search order is:
1.  `/etc/puppetlabs/code/environments/production/heiradata/node1.example.com.yaml`
2. `/etc/puppetlabs/code/environments/production/heiradata/houston.yaml`
3. `/etc/puppetlabs/code/environments/production/heiradata/common.yaml`

### Heira functions

**Heira functions**
- `heira($key)` returns first value found
- `heira_array($key)` creates array of all values found
- `heira_hash($key)` creates a hash of all *hash* values found
- `heira_include($key)`

## Parameterized Classes

Allows you to define a class with default values that can be overriden

### Example

```puppet
class ssh (
  $server = true,       # Enable the server
  $client = true,       # Enable the client
  $allow_root = true,   # permit root to log in
  $untrusted = false,   # permit untrusted hosts to log in
  $x11_forward = false, # forward X1 1 protocol; run remote graphical apps
) {

  include ssh: : hostkeys # set up keys for trusted hosts

  if $server {
    include ssh::server           # manage server
    file { '/etc/ssh/sshd_config':
    ensure => file,
    content => epp('ssh/sshd_config.epp' ),
    }
  }

  if $client {
    include ssh::client           # manage client
    file { '/etc/ssh/ssh_config' :
    ensure => file,
    content => epp('ssh/ssh_config.epp' ),
    }
  }
}
```

### Specify parameter data types

We can also specify parameter data types

```puppet
Boolean $server = true,
```

Types:
- Strings
- Numbers
- Booleans
- Arrays
- Hashes
- Regular Expressions
- Sensitive
- Undef
- Resource References
- Default

### Using parameterized class

```puppet
class profile::ssh::workstation {
  class { 'ssh':
    x11_forward => true,
    server => false,
  }
}

class profile::ssh::bastion {
  class { 'ssh':
    allow_root => false,
    untrusted => true,
  }
}

node 'jumphost.example.com' {
  include profile::ssh::bastion
  # [. . . ]
}

node 'web01.example.com' {
  include ssh # accept all default parameters to the ssh class
  # [. . . ]
}
```

### NC editing of Class Parameters

`Nodes -> Classification -> Classes(tab)`
- `Add new class`
- select `parameter` from dropdown and enter a `value`

### Class Inheritance

Can be used to calculate parameters for example


In `params.pp` we can set up default parameters

```puppet
class apache::params {
  case $facts['os']['family'] {
    'Redhat': { $httpd_user = 'apache' }
    'Debian': { $httpd_user = 'www-data' }
    default: { fail("....") }
  }
}
```

And in your class you can use above defaults

```puppet
class apache (
  $httpd_user   = $apache::params:httpd_user,
  ...
) inherits apache::params {               # Inherit explicitly

  ...
}
```

### Inheritance considered harmful

**Use include instead of inheritance**
- multiple inheritance leads to complex tress
- multiple levels of inheritance makes it hard to know where var was declared

### Automatic Parameter Lookup with Heira

```puppet
 class ntp (
   $time_server,                  # default to hiera('ntp::time_server' )
   $crypto = false,               # default to hiera('ntp::crypto', false)
 ) {
   file { '/etc/ntp.conf':
     content => epp( 'ntp/ntp.conf.epp',
       {
         time_server => $time_server,
         crypto => $crypto,
       }),
   }
 }
```

And in your class you can simple `include ntp`

The heria looks like

```yaml
ntp::time_server: time.puppet.com
```

Order of class parameter resolution is:
1. passed in parameters
2. heira values
3. class defaults

## Puppet Forge

### Command line

`puppet module list --tree`

## Introduction to Roles & Profiles
## Capstone Lab
## Course Conclusion
## Appendix: References

