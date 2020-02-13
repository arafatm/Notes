# Puppet Practitioner

## Intro

### Further reading

[Code Manager](https://docs.puppet.com/pe/latest/code_mgr.html)

### Handouts

["VirtualPractitioner 
pdfs](https://drive.google.com/drive/folders/0BwjXv3TJiWYESDhLTVd6U2xGMDQ)


### Classroom environment

Using Practitioner v4.3.4

CIAB 10.0.9.137
- ssh 2200
- http 8800
- https 4430
- slides 9090

- Gist with notes http://tiny.cc/betapract

### Learning Objectives

- Demonstrate the mastery of fundamental Puppet language constructs.
- Demonstrate the usage of advanced language constructs.
- Build well-architected modules appropriate for sharing with the community.
- Identify and compare common design patterns.
- Troubleshoot and solve problems using data provided by Puppet.
- Identify and follow Puppet Best Practices, and know how to deviate when 
  necessary.

### Course Overview

- A Puppet **Master** with multiple environments backed by git repositories.
- **PuppetDB** as the data warehouse for all Puppet data generated in the 
  classroom.
- **Hiera** as a single source of truth for data lookups in our manifests.
- Shared information to stand up a **web application behind a proxy**.
- A series of modules adhering to **common design patterns**.

### Course Agenda

Day 1
- Puppet basics review
- Using Puppet data for visibility while updating code
- Data structures in the Puppet DSL
- New language constructs introduced in Puppet 4
- Methods for specifying resource relationships and ordering
- Writing custom facts & functions

Day 2
- Alternate ways of managing files, or parts of files
- Best practices pertaining to class inheritance
- Data separation and single source of truth
- Architecting modules and abstraction layers
- Roles & Profiles

Day 3
- Introduction to testing Puppet code
- Sharing modules with the community
- Orchestration with MCollective
- Capstone Lab

## Lesson 3 Puppet Basics Review

### Creating a classroom account

- Create your user http://10.0.9.137:8800
- `ssh arafatm@10.0.9.137 -p 2200`
- Make sure node cert is signed in PE

### Lesson 2: Editing Code

Github -> `$environments/arafatm` -> Agent arafatm

`environments` == `environmentpath` in `puppet master --genconfig | less`

### Configuring a control repository

create a new branch same as **your github id**

Deploy
1. Browse to the Users tab in the Classroom Manager and deploy your code.
  1. Selectyouruserifit'snotalreadyselected.
  2. Press the Deploy Environment button and wait a moment.
2. Navigate to the PE console using the link on the Classroom Manager home page
3. Log in with the same credentials you set for your Classroom Manager account.
4. Using the left navigation bar, navigate to the Nodes->Classification section
5. Select the environment group corresponding to your username.
6. Switch to the Classes tab of your Node Group.
7. Add the examples::[course] class corresponding to the course name:
  - examples::practitioner
8. Commit the change. 

Enforce the new configuration
1. Log into your Agent container.
2. Enforce the new configuration. `puppet agent -t`

:construction: For this course we're not using code manager. Have to hit the 
"Deploy Environment" button in the Classroom Manager (not PE)


### Configure Travis automated builds

https://github.com/carthik/classroom-control-vp/blob/arafatm/.travis.yml

### Lifecycle of a Puppet Agent Run

1. Agent sends Facts to master
2. Master compiles and sends Catalog to agent
3. Agent Reports run to Master
4. Master logs Report

### Facter

`$ facter` generates facts on the agent

### Puppet Resources

Building blocks https://docs.puppet.com/puppet/4.9/type.html e.g.
- Package
- File
- Service
- etc

### Resource Declarations

Always has a `type` and `title` pair that must be **unique**

### Resource Abstraction Layer

similar resources are grouped into **resource types** e.g.
- File: POSIX, Windows
- Package: Gem, Yum, etc
- Service: Launchd, Upstart, etc
- User: AIX, LDAP, etc

Each of the resource types above has **providers** e.g. Gem, Yum, etc

**RAL** can be used to retrieve the state of a resource e.g. `$ puppet resource 
user elvis`

### Exercise 3.1: Edit a Module

### Classifying Nodes

**Classification** is the process of connecting classes to group of nodes

### Classifying Nodes in Code

`$ vi $environment/manifests/site.pp`

```puppet
node /\.puppetlabs\.vm$/ {
  include classroom
}

node 'wallace.puppetlabs.vm' {
  include review
}

node default {
  notify { "Node ${fqdn} has no node definition": }
}
```

:construction: wallace does not get previous include. Not additive.

Can use strings or regular expressions

### Classifying nodes in the PE Console

PE -> Nodes -> Inventory

- Apply classification to *groups* instead of nodes.
- Node groups can also assign *environments*.
- Can add parameters to classes
- site.pp limited to regex to grouping. this is more flexible

`$ puppet agent --configprint environment` to view which environment this node
is in.

Can edit `$ vi /etc/puppetlabs/puppet/puppet.conf` by adding `environment = 
myenv` under `[agent] section`

:construction: Node env is a security concern since I can override the env on 
the node if i have access. but assigning in the console overrides what I set on 
agent.

Node can only be in 1 environment but multiple groups

### Exercise 3.2: Explore Classification

## Lesson 4: Using Puppet Data

### Agent Cached Files

`$ tree $(puppet agent --configprint statedir)` to view useful info

`$ cat $(puppet agent --configprint classfile)` to view what classes are 
applied to this node in last run

`$ grep docker $(puppet agent --configprint classfile)` validates class docker 
is being enforced

`cat $(puppet agent --configprint resourcefile)` lists resource titles enforced 
during last run

`grep yumrepo $(puppet agent --configprint resourcefile)` idenfity which yum 
repos are being managed

### Exercise 4.1 Validating Classifiction

1. Check the timestamp of your classfile
  - `ls -l $(puppet agent --configprint classfile)`
2. Run Puppet and check the timestamp again to see it change.
3. Ensure that the `userprefs` class was enforced on your node
  - `grep userprefs $(puppet agent --configprint classfile)`
4. Check to see that the rc file for your shell is being managed:
   - `grep '/root/.bashrc' $(puppet agent --configprint resourcefile)` 

Inspect the `userprefs` Classification parameters

1 Check the catalog to ensure that the parameters you specified are set.
- `cd $(puppet agent --configprint client_datadir)/catalog`
- `jq '.resources[] | select(.type == "Class" and .title == 
  "Userprefs").parameters' yourname .puppetlabs.vm.json`

2 Inspect the complete Class object to see what other interesting data you 
could use.
 - Press the up arrow and edit the command line to remove .parameters .

3 Use a jq query to determine the list of MCollective middleware hosts.
 - The class name is Puppet_enterprise .
 - The parameter name is mcollective_middleware_hosts .
 - Hint: you saw how we used .parameters to index into the proper subkey.  
 - How do think you might index deeper into the mcollective_middleware_hosts 
   subkey?

 `jq '.resources[] | select(.type == "Class" and .title == 
 "Puppet_enterprise").parameters.mcollective_middleware_hosts' 
 training.puppetlabs.vm.json ["master.puppetlabs.vm"]

### Agent last run report

` $ cat $(puppet agent --configprint lastrunreport)`

`grep -B 25 'changed: true' last_run_report.yaml` to view changed resources 
from last run

### Config Version in Reports

Default in `# $environmentpath/production/environment.conf` is `config_version 
= /bin/date`

Can be set programmatically e.g. 
- `config_version= /usr/local/bin/get_environment_version.:shipit:$environment`

### Event Inspector

View event across all nodes
- Change
- Failure
- No-op
- Skip

:warning: 
- won't show events that restart PuppetDB
- won't show runs without events
- time sync is important
- coalesced event display: displays ensurables types creation as single event

### Exercise 4.2: Puppet Run Reports

- Examine a Puppet report.
- Configure a custom `config_version` script.

1 See what changes were made in the last Puppet run
- `grep -B 25 'changed: true' $(puppet agent --configprint lastrunreport)`

2 If no changes appeared, make a minor modification to a managed file
- `vim /root/.bashrc.puppet`, or
- `vim /root/.zshrc.puppet puppet agent -t`

3 Take a look at the raw data in a report
- `vim $(puppet agent --configprint lastrunreport)`

Validate your existing environment version

1 Run the Agent and check its configuration version. puppet agent -t

Expected output
`Applying configuration version '1489778215'`

Configure a config_version for your environment

1 Add config_version to your environment by editing the environment.conf file.  
- Physical classes:
  - `vim ~/puppetcode/environment.conf` 
  - Commit and push to the master.

- Virtual classes:
   - Edit [control-repo]/environment.conf
   - Deploy your codebase.

 2 Run the Agent and check its new configuration version.
 - `puppet agent -t`

 3 Compare the configuration version to that of your development repository.  
 - Physical classes:
   - `git rev-parse --short HEAD`
 - Virtual classes:
   - See the most recent commit listed for your branch of the control repository

Example file: [environment]/environment.conf

```puppet
  modulepath = site:modules:$basemodulepath
  config_version = '/usr/local/bin/get_environment_version.:shipit:$environment'
```

### Checkpoint: Using Puppet Data

How does Puppet expose the data it creates?

Which statements are true about the Puppet Enterprise Event Inspector?
- The Event Inspector provides a simple way to trigger Puppet agent runs on 
  individual nodes.
- The Event Inspector allows you to observe live results of individual Puppet 
  agent runs.
- ✓ The Event Inspector collates and displays events instead of reports.
- ✓ The Event Inspector can show you which nodes have restarted Apache 
  recently.

The Puppet agent saves copies of:
- ✓ The last report generated.
- Copies of catalogs for each node.
- ✓ A summary of the last run.
- ✓ A list of all classes enforced on that machine.

The config_version script is often used to:
- Correlate a Puppet agent run with the codebase repository revision used to 
  generate it.
- Halt catalog compilation if the codebase is not using the proper version.
- Check out the proper codebase revision before the catalog is compiled.

## Lesson 5: Resource Types

### Objectives

- Use resource defaults to reduce duplication.
- Purge non-managed resources.
- Define and declare your own resource types.
- Explain the utility of defined resource types.

### Resource Defaults

This code block will apply to all `file` resources as default

```puppet
File {
  owner => 'root',
}
```

Scope only applies to what follows (must be declared before usage). **parse 
order dependant**

:warning: ^ not predictable. if multiple classes include foo we can't guarantee 
which resource defaults will get applied in foo

Can also `include bar` after above declaration to have it apply

### Resources Resource

```puppet
resources { 'user':
  purge => true,
  unless_system_user => true,
}
```

This will remove all users not explicitly declared

### Exercise 5.1 Resource Purging

Objective:
- Use Puppet to purge unmanaged host records.
- Experiment with the resources resource.

### Defined Resource Types

```puppet
define apache::vhost (
  ...
) {
  ...
}
```

To use

```puppet
apache::vhost { 'elmo.puppet.com':
  ...
}

apache::vhost { 'kermit.puppet.com':
  ...
}
```

Organized in modules just like a class

`.../modules/apache/manifests/vhost.pp`

### Exercise 5.2 Defined Type

Objective:
- Create a `managed_user` type.
- Manage content in users' home directories.

### Checkpoint: Resources

Which of the following are common ways to specify default values for new resources?
- ✓ Using the resource default syntax
- Setting the $defaults variable to a hash of default values
- Set default values for each resource type in puppet.conf

Using an array as a resource title will enforce resources in the order they're 
listed in the array
- True
- ✓ False

What are some benefits to using defined types?
- ✓ They show what you intend to do.
- Ensure that Puppet runs exec commands in the proper order.
- Ensure that the enforced state is always consistent.
- Encourage you to maintain semver to compatibility.

## Lesson 6: Language Constructs

### Core data types

| String             | 'Hello World'
| Number             | 42
| Boolean            | true
| Array              | ['1', '2']
| Hash               | { 'key' => 'value' }
| Regular Expression | /^web\d{3}/
| Resource Reference | File['/etc/motd']

### Abstract Data Types

| Data Type | Example
| --        | --
| Optional  | `Optional[String]`
| Variant   | `Variant[Integer, Float]`
| Pattern   | `Pattern[/\A[a-z].*/]`
| Enum      | `Enum['stopped', 'running']`

### Asserting a Data Type

- `=~` and `!~` match operators accept a data type on the right side.
- `assert_type()`


### Exercise 6.1: Validating Parameters

Objective:
- Update a class to validate parameters with data types.

### Lambdas

Similar to **anonymous functions**

```puppet
$binaries = ["cfacter", "facter", "hiera", "mco", "puppet", "puppetserver"]

 # link each binary into /usr/local/bin for convenience
$binaries.each |String $binary| { 
  file { "/usr/local/bin/${binary}":
    ensure => link,
    target => "/opt/puppetlabs/bin/${binary}",
  }
}
```

| Call Style          | Example
| ------------------- | -------------------
| Classic prefix      | `upcase("some string")`
| Chained             | `"some string".upcase`
| Prefix with lambda  | `each($packages) | $pkg | { ... }`
| Chained with lambda | `$packages.each | $pkg | { ... }`

### Iteration Functions

 | `each`   | Run a lambda for each element of an array or hash.
 | `slice`  | Run a lambda once for each group of elements
 | `filter` | Use a lambda to select a subset of elements.
 | `map`    | Use a lambda to transform every value
 | `reduce` | Sum up values from a data structure with a lambda.

### Readability

```puppet
notice Integer[1,99].map |$x| {
  case [$x, $x % 3, $x % 5] {
    [default, 0, 0]       : { fizzbuzz }
    [default, 0, default] : { fizz }
    [default, default, 0] : { buzz }
    default               : { $x }
  }
}
```

### Map Reduce (filter)

`filter()`
- Select all items for which the lambda returns truthy.

`map()`
- Applies a lambda to each item in an array or hash.
- Returns an array of the results of each invocation.
- Does not affect the original sequence

### Exercise 6.2

Use the each function to declare multiple resources.

### Checkpoint: Language Constructs

How do the new iteration functions work?

Variables declared within the block associated with an iterator function are 
accessible outside that block.
- True
- ✓ False

Proper use of iterators eliminates the need for readable code.
- True
- ✓ False

Resources declared within iterator function blocks must have unique titles.
- ✓ True
- False

Using abstract data types to validate your parameters allows you to:
- ✓ specify a list of allowed values. `enum`
- ✓  specify a regular expression that a string must match.
- ✓ specify that a parameter must match a given data type or remain undefined 
  (undef).
- ✓ specify an array of valid data types.

## Lesson 7: Ordering Techniques

### Objectives

- Explain parse order dependence and resource dependencies.
- Understand class and resource containment.
- Use alternate syntax to describe order.
- Assign ordering relationships based on search expressions.

### Abbreviations

- `before` applies this resource **before**
- `require` applies this resource **after**
- `notify` applies this resource **before** and **refreshes**
- `subscribe` applies this resource **after** and **refreshes**

- `->` applies resource on **left before right**
- `<-` applies resource on **right before left**
- `~>` applies resource on **left before right** and refreshes
- `<~` applies resource on **right before left** and refreshes

```puppet
package { 'httpd': ... }
file { '/etc/httpd/conf/httpd.conf': }

Package['httpd'] -> File['/etc/httpd/conf/httpd.conf']
```

or 

```puppet
exec { ... } ~>
exec { ... }
```

2nd pattern is less readable

### Catalog Graph Files `relationships.dot`

```
$ tree $(puppet agent --configprint graphdir)
├── expanded_relationships.dot
├── relationships.dot
└── resources.dot
```

`puppet catalog --render-as dot find localhost > catalog.dot` to generate a 
graph by rendering a catalog as dot format

Can paste your code and click on `show relationships` to view the graph on 
https://validate.puppet.com/validate

### Containmnent Problem

`include` is idempotent. Works similar to *require_once* in other langs
- included classes are **not contained** and the **order is not guaranteed**

```puppet
class repos {
  include site::secure
  ...
}
class apache {
  include site::secure
  ...
}
```

`site::secure` *floats* outside of repos and apache

### Ensuring Classes are Included

`include` sets **no ordering** relationship

`require` also ensures class is enforced **before** current

`contain` ensures class is contained **within** the current one

**warning** best practice is to only contain classes from withing **same 
module**

See https://puppet.com/blog/class-containment-puppet or distinction between 
require and contain

:warning: the more require and contains you have, the greater the chance of a 
dependency cycle conflict and it takes longer to compile the catalog

### Console Node Graphs

`Configuration -> Overview` to view class containment

### Exercise 7.1: Ordering Methods

- Practice using class containment and relationships.
- Evaluate different ordering techniques.

### Ordering across nodes (Exporting Resources)

Export resources to a DB then collect and use them on other nodes
- Used to share information
- Cross node order dependencies

:warning: requires a DB backend e.g. PuppetDB

```puppet
class hosts {
  # create a virtual host resource based on known information
  # and export it back to the Puppet Master
  @@host { $::fqdn:
    ip           => $::ipaddress,
    host_aliases => $::hostname,
  }

  # collect all exported resources and realize them on this host
  Host <<| |>>

  # ensure that we have no host entries that aren't explicitly configured
  resources { 'host':
    purge  => true,
  }
}
```

`@@` markes the virtual resource as exportable

`<< >>` collects and realizes exported virtual resources

### Exercise 7.2 Export a Resource

### Checkpoint: Ordering Techniques

What are some ways to influence resource enforcement ordering?

The -> chaining arrow explicitly represents which dependency metaparameter?
- before
- require
- ✓ either

The contain() function should always be used instead of include().
- True
- ✓ False

The Console Node Graph shows you explicitly what order all resources will be
applied in
- True
- ✓ False

Exporting resources could simplify which of these use cases?
- ✓ Informing a firewall of a port that should be opened for a managed 
  application.
- ✓ Ensuring that a node is authorized to open a remote database connection.
- Recording which packages are installed on all managed nodes. (can use PDB 
  instead)
- ✓ Ensure that clustered webservers only get traffic once the web application 
  is configured.

## Lesson 8: Facts and Functions

### Objectives

At the end of this lesson, you will be able to:
- Identify the lifecycles of facts and functions.
- Access facts in your Puppet manifests.
- Execute functions in your Puppet manifests.
- Develop simple facts and functions.

### Facts

`$ facter os` can be used in catalog as:

```puppet
case $facts['os']['release']['major'] {
```

### Custom Facts

```
$ tree /etc/puppetlabs/code/environments/production/modules/custom
├── lib
│   ├── facter
│   │   └── role.rb
```

Write **custom fact** in `role.rb`

```ruby
Facter.add('role') do
  setcode 'cat /etc/role'
end
```

This code goes on the *master* and is **pluginsync**'d to the agent

Simple fact to determine the role of a server in `role.rb`

```ruby
Facter.add('role') do
  setcode do
    role = Facter::Core::Execution.exec('cat /etc/role')
    role.gsub(/<.*?>/m, "")
  end
end
```

Use `$ facter -p role` to view pluginsynced fact

To test facts locally you have to set `FACTERLIB` or `RUBYLIB`

```
$ export PROD=/etc/puppetlabs/code/environments/production/
$ export RUBYLIB=${PROD}/modules/custom/lib
$ facter role
```

Can also create `json/yaml/txt` files on the **agent** e.g.  
`/etc/puppetlabs/facter/facts.d/myfacts.txt`

### Exercise 8.1: Create a Custom Fact

Objective:
- Create and use a new custom fact.
- Practice exposing client information for use during catalog compilation.

### Functions

Either a `:statement` or `:rvalue`

```
$ tree /etc/puppetlabs/code/environments/production/modules/custom/
├─ lib
│  └─ puppet
│    └─ parser
│      └─ functions
|        └─ mastername.rb ## $mastername = mastername()
```

A custom `:statement` function:
```ruby
Puppet::Parser::Functions.newfunction(:myfunc) do |args|
  # ...
end
```

A custom :rvalue function:
```ruby
 Puppet::Parser::Functions.newfunction(:myfunc2, :type => :rvalue) do |args|
   # ...
end
```

### Custom Functions

Example custom funtion in `mastername.rb`

```puppet
require 'socket'

module Puppet::Parser::Functions
  newfunction(:mastername, :type => :rvalue ) do |args|
    Socket.gethostname.chomp
  end
end
```

To pass arguments set the defined number of expected arguments with `:arity => 
1` and can be accessed with `args[0]`

### Exercise 8.2: Create a Custom Function

Objective:
- Write and use a custom function.
- Practice adding functionality to the Puppet DSL.

:shipit: skipped

### Checkpoint: Facts and Functions

How can custom facts and functions be used?

Accessing a fact variable in a manifest results in the master requesting that 
fact from the agent. 
- True
- ✓ False

Every fact is gathered before the master even begins to compile the catalog.  
- ✓ True
- False

Function arguments are automatically converted to an array. 
- ✓ True
- False

Which of these statements are true?
- ✓ Facts and functions in modules are distributed automatically.
- Functions are only used when enforcing a catalog.
- Fact values can change during the compilation and enforcement of a catalog.
- ✓ By default, a function returns no value.

## Lesson 9: File Manipulation

### Objectives

At the end of this lesson, you will be able to:
- Identify several techniques for managing parts of files as resources.
- Iteratively create configuration files out of component pieces.
- Interact with configuration settings contained in files.

### `file_line` Resource

`file_line` is included in **puppetlabs/stdlib**. Allows editing a **single 
line** in a file

```puppet
  # Configure tools to use local proxy server
file_line { 'bashrc proxy setting':
  ensure => present,
  path   => '/etc/bashrc',
  line   => 'export HTTP_PROXY=http://squid.puppetlabs.vm:3128',
  match  => '^export\ HTTP_PROXY\=',
}
```

Leaving out `match` will append the `line`

### File fragments using `Concat`

Allows editing of **sections** of a file and is ordered with `order`

```puppet
$motd = '/etc/motd'

concat { $motd:
  ...
}

concat::fragment { 'foo':
  target => $motd,
  content => 'foo'
  order => '01',
}
```

### Other file manipulation options

- `puppetlabs/inifile` ini
- `herculesteam/augeasproviders_sysctl` sysctl.conf
- `fiddyspence/hash_file` yaml/json

### Exercise 9.1: Managing File Content

Objective:
- Use Puppet resources to manage only parts of files.
- Evaluate different file manipulation patterns.

Extra Credit:
- Create a defined type to abstract file manipulation.

### Augeas Configuration Setting Management Tool

`$ /opt/puppetlabs/puppet/bin/augtool`

```puppet
augeas { 'yum.conf':
  context => '/files/etc/yum.conf/main',
  changes => 'set proxy http://squid.puppetlabs.vm:3128',
}
```
This changes the proxy setting to `proxy=http://squid...`

### Checkpoint: File Manipulation
What are some techniques for managing parts of files?

Augeas can be used to manage any kind of file.
- True
- ✓ False

Which of these patterns would you use to manage a single setting in 
puppet.conf?
- file_line
- concat
- ✓ augeas

Which of these patterns would you use to add a "last Puppet run" timestamp to /etc/motd?
- ✓ file_line
- concat
- augeas

Which of these patterns would you use to manage stanzas in an application 
configuration file?
- file_line
- ✓ concat
- augeas

## Lesson 10: Inheritance

:warning: **don't use inheritance**

### Objectives

At the end of this lesson, you will be able to:
- Describe the uses of class inheritance.
- Abstract common behaviours into base classes.
- Describe variable resolution through parent classes. Utilize design patterns 
  to simplify platform abstraction.
- Identify drawbacks to inheritance and clearer alternatives.

### Inherited Classes

```puppet
class ssh::paranoid inherits ssh {
```

Classes may only have one parent.

Variables resolve in order: local scope -> parent scope -> ... -> node scope -> 
global scope

### Params Class Pattern

```puppet
class apache::params {
  case $facts['os']['family'] {
    ...
  }
}

class apache inherits apache::params {
  ...
}
```

Params pattern allows local access

### Checkpoint: Inheritance

How does class inheritance work in Puppet?

In which of these situations is inheritance required?
- When sharing common resources in a single base class.
- ✓ When you must override resource parameters.
- ✓ When using the params.pp pattern.
- When overriding facts defined by a node.

Best practices say that you should use inheritance when?
- When sharing common resources in a single base class.
- When you must override resource parameters.
- ✓ When using the params.pp pattern.
- When overriding facts defined by a node.

The params.pp pattern should be used to calculate platform defaults
- ✓ True
- False

What pattern should usually be used instead of inheritance?
- Indeterminance
- ✓  Composition
- Parameterization

## Lesson 11: Data Separation

### Objectives

At the end of this lesson, you will be able to:
- Describe the single source of truth design pattern.
- Identify the data abstraction capabilities of Hiera.
- Identify available Hiera functionality in Puppet.
- Configure and use Hiera.
- Describe the role of Automatic Parameter Lookup.

### Problem Statement

Conflating **code** and **data** causes maintenance issues.

**Heira** as a single source of truth

### Heira

Can allow use of modules by overriding data without editing code

Has multiple backends e.g. `cmdb`, `yaml`, `json`, `heira-eyaml`, etc

sample `${datadir}/environments/development.yaml`

```yaml
ntpserver: 212.22.1.3
dnsservers: [ "10.0.0.1", "10.0.0.2" ]
```

Hiera will search for key value pairs in the following order:
1. /etc/puppetlabs/code/hieradata/hosts/agent.puppetlabs.vm.yaml
2. /etc/puppetlabs/code/hieradata/environments/development.yaml
3. /etc/puppetlabs/code/hieradata/common.yaml

```puppet
$ntpserver = hiera('ntpserver')
```

Sample hiera config file in `/etc/puppetlabs/puppet/hiera.yaml`

```yaml

---
:hierarchy:
  - "%{clientcert}"
  - "%{environment}"
  - common
  - global

:backends:
  - yaml

:yaml:
  :datadir: /etc/puppetlabs/code/hieradata

```
### Heira Functions

- `hiera` returns the first value found for a key
- `hiera_array` returns an array of all matching values for a key
- `hiera_hash` returns a merged hash of all matching values for a key
- `hiera_include`
  - includes each of an array of class names returned from a hiera_array() call
  - can be used as a lightweight External Node Classifier (ENC)

### hiera()

```bash
$ cat ${environment}/hieradata/hosts/kermit.puppetlabs.vm.yaml

---
smtp::server: 'smtp.puppetlabs.vm'
smtp::run_as: 'svc.smtp'
```

```puppet
$run_as = hiera('smtp::run_as')
```

### hiera_array()

```bash
$ cat /etc/puppetlabs/code/hieradata/common.yaml

---
packages: [ 'ruby', 'php', 'mysql' ]

$ cat /etc/puppetlabs/code/hieradata/environments/development.yaml

---
packages: [ 'ruby-devel', 'php-devel', 'mysql-devel' ]
```

```puppet
package { $package_array: ... }
```

### hiera_hash()

```bash
$ cat /etc/puppetlabs/code/hieradata/common.yaml 

  ---
  users::sysadmins:
    gary:
      shell: /bin/bash
      uid: 501

$ cat /etc/puppetlabs/code/hieradata/environments/development.yaml

  ---
  users::sysadmins:
    craig:
      shell: /bin/bash
      uid: 502
```

`heira_hash('users::sysadmins')` will return both gary and craig

### hiera_include()

- Returns
- Can be used as a lightweight ENC.

```bash
$ cat /etc/puppetlabs/code/hieradata/hosts/kermit.puppetlabs.vm.yaml
  ---
  purchased::services: [ 'mysql_server','httpd','wordpress']

$ cat /etc/puppetlabs/code/hieradata/hosts/oscar.puppetlabs.vm.yaml
  ---
  purchased::services: [ 'pgsql_server','nginx','drupal']
```

```puppet
class purchased {
  hiera_include('purchased::services')
}

node 'kermit.puppetlabs.vm' {
  include purchased
}
```

`class purchased` automatically includes the array of `purchased:serverces` as 
classes

### Automatic Parameter Lookup

Class parameters are automatically looked up from Hiera.

Hiera keys queried are `class::param`

`# /etc/puppetlabs/code/hieradata/common.yaml`
```yaml

---
ntp::time_server: time.puppet.com
```

```puppet
class ntp (
  $time_server,     # automatically uses hiera('ntp::time_server') as default 
  $crypto = false,  # automatically uses hiera('ntp::crypto', false) as default
){
  file { '/etc/ntp.conf':
    content => epp('ntp/ntp.conf.epp',
      { time_server => $time_server, crypto => $crypto }),
  }
}
```

### hiera-eyaml

```yaml

---
plain-property: You can see me

encrypted-property: >
  ENC[PKCS7,Y22exl+OvjDe+drmik2XEeD3VQtl1uZJXFFF2NnrMXDWx0csyqLB/2NOWefv
  [...]
  IZGeunzwhqfmEtGiqpvJJQ5wVRdzJVpTnANBA5qxeA==]
```

### node_encrypt

wipes sensitive data in catalog and reports.

```puppet
node_encrypt::file { '/tmp/foo':
  owner => 'root',
  group => 'root',
  content => 'This string will never appear in the catalog.',
}
```

### Exercise 11.1: Configure Hiera

Objective:
- Configure and test Hiera on your Puppet Agent.
- Retrieve Hiera data from the Puppet Master.
- Practice data abstraction.

### Checkpoint: Data Separation

How should you keep configuration data separated from the code that configures 
your nodes based on that data?

Hiera allows you to use only one backend at a time
- ✓ True
- False

The single source of truth design pattern allows you to:
- Point your finger at the dev who checked in bad code.
- ✓  Ensure that updates propagate everywhere they're needed.
- Cut and paste with confidence.
- ✓ Ensure that each application that uses a common setting has the same value 
  for that setting.

Which of these functions can return an array?
- hiera
- ✓ hiera_array
- hiera_hash
- ✓ hiera_include

## Lesson 12: Architecting Modules

Objectives; At the end of this lesson, you will be able to:
- Define the appropriate scope for new modules.
- Structure new modules effectively.
- Design modules for future maintainability.
- Create composable component modules that are reusable.

### Each module should focus on one thing

Make focused classes that are **reusable** and **composable**

### Class layout

Configuration stages should be abstracted by classes.

Module main class `init.pp`
- Main interface point.
- The only parameterized class, if possible.
- Control behaviour of the entire module by declaring a single class.
- Provide sensible defaults for all parameters.

`module::install` Resources used to install all managed packages or software.

`module::config` Resources and logic used in configuring the managed software.

`module::service` Resources used to manage the running state of any services.

### Parameters class

Main class should **inherit** `modules::params.pp`

```puppet
class ntp (
  $autoupdate = $ntp::params::autoupdate,
  $config = $ntp::params::config,
  ...
) inherits ntp::params {
```

Only inherit params in main class.

### Module dependencies

**require** sub classes in the module

```puppet
class drupal {
  require drush
  contain drupal::install
  contain drupal::configure
  ...
}
```

### Data Separation

Data that should be stored in **Hiera**
- Business or site specific data:
  - Internal NTP server.
  - VIP address
- Sensitive or private data.

Data that should be calculated in the **params** class
- Data that everyone who uses this module needs.
- OS-specific data:
  - Paths to config files.
  - Package names.

### Code Defensively

It is better to **fail compilation** than to enforce unpredictable 
configuration

```puppet
case $facts['os']['name'] {
  ...
  default : { fail("Unsupported platform ${facts['os']['name']}") }
}
```

```puppet
class myservice(
  # Catalog compilation will fail for values that are neither
  # 'stopped' nor 'running'
  Enum['stopped', 'running'] $ensure = 'running'
```

### Checkpoint: Architecting Modules

How should Puppet modules be designed to maximize reusability and future 
maintainability?

What are good design goals to keep in mind when architecting a new module?
- ✓ How the module could be reused in other contexts.
- Manage as much as possible in a single module to avoid dependencies.
- ✓ How the module could be combined with other modules to provide greater 
  customizability.
- Whether the manifest files should have Windows line endings.

Why is it useful to have subclasses such as ::install and ::service?
- ✓ Class dependencies mean that the class internals can be refactored at will.
- ✓ Each subclass has a single specific task, which makes it easier to read.
- It's a lot less typing.
- ✓ The main class only includes dependencies and subclasses, leading to 
  clarity.

Clarity is more important than being clever.
- ✓ True
- False

## Lesson 13: Roles and Profiles

### Objectives

At the end of this lesson, you will be able to:
- Identify drawbacks to node level logic.
- Differentiate between business logic and implementation.
- Use Hiera and the ENC to efficiently abstract layers of the stack.
- Create appropriate role and profile classes.

:warning: Roles/Profiles is a pattern, not a builtin function

### Danger Signs

- Resources declared in multiple modules.
- You find yourself wondering where your implementation fits.
- Copious amount of logic at a node level.
- Repetition and duplication.
- The if statement is your best friend.

### Good Design - Appropriate Abstraction Layers

Good modules should:
- only manage their own resources.
- be granular and portable.
- avoid exposing implementation details.

Good architecture should:
- provide business logic to classification.
- provide an abstraction layer for implementation of components.
- make code adaptable to complex requirements.
- reduce node-level logic.
- reduce functionality overlap.

**profile class** := A wrapper class that declares one or more *component* 
classes customized to local needs as part of a layered technology stack.

### Abstraction Layers

- Data is abstracted by **Hiera**.
- Providers are abstracted by **types**.
- Resources are abstracted by **classes**.
- Classes are abstracted by **modules**.
- Component Modules are abstracted by **profiles**.

### Example implementation

```puppet
class profile::myapp (
  $database_host = 'localhost',
) {
  include tomcat
  include mysql

  class { '::myapp':
    db_engine => 'mysql',
    db_host => $database_host,
  }
}
```

### Use Composition for Abstraction

```puppet
class profile::application {
  contain tomcat
  contain mysql
  contain profile::common::config
}

class profile::application::myapp {
  require profile::application

    class { '::myapp':
      db_engine => 'mysql',
      db_host => 'localhost',
    }
}

class profile::application::myotherapp {
  require profile::application
  class { '::myotherapp':
    db_engine => 'mysql',
    db_host => 'localhost',
    smtp_host => hiera('smtp_host'),
  }
}
```

### Exercise 13.1: Designing Profiles

Objective:
- Design profile classes for several technology stacks.
- Practice identifying appropriate levels for abstraction.

### Roles

Represents the **business logic** not the implementation
- Profile => implementation
- Role => business need

Roles **only implement** profiles

```puppet
class role::webapp {
  include profile::base
  include profile::customapp
  include profile::test_tools
}
```

### Classifying Nodes

A Node should have a **single** role.
- if node has 2 roles => new role

```puppet
node 'craig.vm' {
  include role::database_control_panel
}
```

OR in PE Console
- `Add a new class` = `role::...`

### Exercise 13.2: Designing Roles

Objective:
- Design roles for the profile classes from the previous lab.
- Practice identifying appropriate levels for abstraction.

### Checkpoint: Roles and Profiles

Which of these are or should be represented as component modules?
- ✓ The puppetlabs/apache module.
- Your company's use of Drupal, PostgreSQL, and Apache.
- ✓ A general module designed to manage Postfix.
- An apache webserver configuration using the puppetlabs/apache module.

What guidelines determine the definition of a role?
- ✓ A node role should serve a single business purpose.
- ✓ A role should be defined as the job it does rather than the tooling chosen 
  for the job.
- You should search the Puppet Forge for role modules before building your own.
- The role module should have a params class to calculate defaults for all 
  roles.

Profiles should be designed to be general and reusable for Forge publication
- True
- ✓ False

## Lesson 14: Module Testing

### Objectives

- Describe unit, integration, and acceptance testing.
- Develop rspec unit tests to effectively test your Puppet code.
- Develop acceptance tests with serverspec to test the end result.

### rspec-puppet

```puppet
require 'spec_helper'

describe('motd', :type => :class) do

  let(:node) { 'testhost.example.com' }

  context 'when called with no parameters on redhat' do

    let(:facts) { { :osfamily => 'RedHat' } }

    it {
      should contain_file('/etc/motd').with({
        'ensure' => 'file',
        'owner' => 'root',
        }).with_content(/^Welcome to #{node}.*$/)
    }

  end
end
```

To run it
```bash
$ PATH=/opt/puppetlabs/puppet/bin/rake spec \
  /opt/puppetlabs/puppet/bin/ruby -S rspec spec/classes/motd_spec.rb --color
```

### RSpec Matchers

- Validate successful catalog compilation: `it { should compile }`
- Validate the catalog contains resources: `contain_<type>`
  helpers for each resource type
- Validate that resources have specified attributes: `with_<attribute>` and
  `without_<attribute>`
- Validate that resources have relationships set: `that_<relationship>`
  for each relationship
- Shortcut helpers that combine matchers: `with` and `without`

### Full example

```puppet

require 'spec_helper'

describe('base', :type => :class) do
  let(:node) { 'testhost.example.com' }

  describe 'when called with no parameters on redhat' do
    let(:facts) { { :osfamily => 'RedHat' } }

    it { should contain_service('ssh') }
    it { should contain_file('foo').with_content(/bar/) }
    it { should contain_file('/etc/sysctl.conf').with_owner('root') }
    it { should contain_file('/etc/my.cnf').that_notifies(Service[mysql]) }
    it {
      should contain_file('/etc/motd').with({
        'ensure' => 'file',
        'owner' => 'root',
      }).with_content(/^Welcome to #{node}.*$/)
    }
    it {
      should contain_service('apache').with(
        'ensure'     => 'running',
        'enable'     => 'true',
        'hasrestart' => 'true',
      ).without(
        'status' => /.*/,
        'start'  => /.*/,
        'stop'   => /.*/,
  end
end
```

### Using puppetlabs_spec_helper

Installing
1. Install rspec-puppet `/opt/puppetlabs/puppet/bin/gem install rspec-puppet`
2. Install puppetlabs_spec_helper to setup tests.  
   `/opt/puppetlabs/puppet/bin/gem install puppetlabs_spec_helper`

Configuring
1. Create your module `puppet module generate <username>-<modulename>`
2. Create `Rakefile`
  - `require 'puppetlabs_spec_helper/rake_tasks'` 
3. Update `spec/spec_helper.rb`
  - `require 'puppetlabs_spec_helper/module_spec_helper'`
4. Create `.fixtures.yml`
```
fixtures:
  symlinks:
    "motd": "#{source_dir}" # Symlink to the root of the module
```

- `symlinks`: Installs your module as a symlink
- `repositories`: Installs modules from git repositories. Can specify branch or 
  tag
- `forge_modules`: Installs modules from the Forge

### Exercise 14.1: Unit Test a Class

- Update an in-house module and create unit tests for it.
- Practice setting up a testing environment.
- Practice incremental development using tests as validation.

### Acceptance Test with `serverspec`

Install/Configure
```bash
$ gem install serverspec
$ mkdir serverspec && cd serverspec
$ serverspec-init
```

`# spec/localhost/httpd_spec.rb`
```puppet
require 'spec_helper'

describe package('httpd') do
  it { should be_installed }
end

describe service('httpd') do
  it { should be_enabled }
end

describe port(80) do
  it { should be_listening }
end

describe file('/etc/httpd/conf/httpd.conf') do
  its(:content) { should match /ServerName localhost/ }
end
```

To run `$ rake spec`

### Exercise 14.2: Acceptance Test a Server

- Use acceptance testing to validate the results of a Puppet Agent run.
- Practice designing acceptance tests.

### Checkpoint: Module Testing

Serverspec acceptance tests should:
- ensure that the Puppet agent run completed successfully.
- ensure that only a single Puppet agent run is required.
- ✓ not concern themselves with the process by which a node is configured.
- test only a single module or class.

Unit tests with rspec can directly replace smoke tests with puppet apply
- True
- ✓ False

Unit tests are designed to ensure that a catalog applies cleanly
- True
- ✓ False

## Lesson 15: Sharing Modules

### Objectives

- At the end of this lesson, you will be able to:
- Define the scope for community oriented modules.
- Construct module releases with proper versioning and metadata.
- Publish modules and releases on the Puppet Forge.

### Modules

Use **semver**

Sign up on forge

Sample metadata.json for auto management

```bash
$ cat mysql/metadata.json

  {
    "name": "puppetlabs-mysql",
    "version": "3.1.0",
    "author": "Puppet, Inc.",
    "summary": "Installs, configures, and manages the MySQL service.", "license": 
    "Apache-2.0",
    "source": "git://github.com/puppetlabs/puppetlabs-mysql.git", "project_page": 
    "http://github.com/puppetlabs/puppetlabs-mysql", "issues_url": 
    "https://tickets.puppet.com/browse/MODULES",
    ...
    "dependencies": [
      {"name":"puppetlabs/stdlib", "version_requirement":">= 3.2.0" }, 
      {"name":"nanliu/staging", "version_requirement":"1.x" }
    ]
  }
```

`puppet module build` to generate the module then publish

## Lesson 16: Orchestration with MCollective

### Objectives

- Identify core MCollective technologies.
- Identify message transport functionality.
- Recall Puppet and MCollective terminology differences.
- Use MCollective to interact with Puppet nodes.
- Generate inventory reports using MCollective.

### MCollective

Terminology:
- **Server**:
  - App server for hosting Agents and managing middleware connection.
  - Runs on every peer, both Puppet Master and Agent.
- **Agent**:
  - Block of Ruby code that performs a specific set of tasks, or Actions.
  - Runs as a plugin of the server.
- **Action**:
  - Tasks exposed by an Agent.
  - An exim queue agent might expose actions like mailq , rm , retry , etc.
- **Application**:
  - MCollective command plugin that sends messages to agents.

`$ mco ping`

Command Structure `mco [APPLICATION] [ACTION] [ARGUMENTS] [OPTIONS]`
- APPLICATION The name of the application you intend to run.
- ACTION The action that should be passed to listening agents.
- ARGUMENTS Arguments that should be passed to the action.
- OPTIONS Options to the mco command.

`$ mco inventory agent.example.com`

Can filter `--with-fact`, `--with-class`, `--with-identity`, etc

`$ mco ping --with-fact osfamily=RedHat`

### Puppet Integration

Example puppet usage
- `mco puppet runall -F osfamily=Debian 5` Run Puppet on 5 Debian nodes at a 
  time
- `mco puppet disable -C dev` Temporarily disable Puppet on dev classified 
  nodes
- `mco puppet summary -I proxy.puppetlabs.vm` Retrieve the last run summary 
  from a node

Example package usage
- `mco package install httpd -C backend` Install a package on classified nodes
- `mco package update httpd -I alphonse.puppetlabs.vm` Update a package on a 
  named node
- `mco package status httpd -F osfamily=RedHat` Retrieve package versions from 
  all RedHat machines

Example `service` usage
- `mco service travis-ci restart -C travis` Restart a service on all travis 
  classified nodes
- `mco service exim stop -I compromised.puppetlabs.vm` Stop a service on a 
  named node
- `mco service exim status` Discover how many mailservers are running

Inventory Reports
- `mco inventory --script inventory.mc`

printf style in a `inventory.mc`
```ruby
inventory do
  format "%s:\t\t%s\t\t%s"
  fields { [ identity, facts["serialnumber"], facts["productname"] ] }
end
```

`$ mco inventory --script inventory.mc`

### Checkpoint: Orchestration

Orchestration makes which of these tasks easy?
- ✓ Check the version of an installed package across your infrastructure
- Provisioning of cloud instances in EC2 and VSphere.
- ✓ Restart Apache on all your webservers
- Edit the Puppet code running on your Master
- ✓ Install cowsay on your neighbor's machine

MCollective allows you to temporarily stop the Puppet Agent on a node.
- ✓ True
- False

If the Puppet Agent is stopped, MCollective will not be able to restart it.
- True
- ✓ False

MCollective allows you to perform actions on a subset of nodes identified by a 
filter.
- ✓ True
- False

## Capstone Lab


# Misc Notes

If class A `include` B, we cannot ensure that B has A's params since order 
isn't guaranteed
- `require` will guarantee availability
- order of params parsing =
  1. Console params
  2. Heira
  3. site.pp
  4. `inherit`

To test control-repo check out https://github.com/dylanratcliffe/onceover


# Remaining

Capstone Lab
Course Conclusion
Puppet Basics Refresher
Appendix
