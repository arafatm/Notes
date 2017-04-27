# Puppet Learning VM

# Setting up the Learning VM

Before starting the VM for the first time, you will need to adjust its
settings. Allocate
- 2 CPUs
- 4GB of memory
- Network Adapter to Bridged

Boot VM and note <IPADDRESS>
- ssh root@<IPADDRESS>
- http://<IPADDRESS> Quest Guide
- https://<IPADDRESS> PE console (note the https)

# Quests

## Welcome

    quest begin welcome

    puppet -V

    quest --help

    quest status

## The Power of Puppet

### Get Started

    quest begin power_of_puppet

### Forge Ahead

    puppet module search graphite

    puppet module install dwerder-graphite -v 5.16.1

To see the modules installed

    ls /etc/puppetlabs/code/environments/production/modules/

If you don't have internet access, modules used in quests are included on vm

    mv /usr/src/forge/* /etc/puppetlabs/code/environments/production/modules

### Class and Classification

To find the ip of the vm:

    facter ipaddress

Access *PE Console* at `https://IPADDRESS`
- username: admin
- password: puppetlabs

### Create a Node Group

Create a Learning VM node group on the console
- Click on `Nodes`
- Click on `Classification`
- `Add group` "Learning VM"
  - `Parent` "All Nodes"
  - `Environment` "production"

Click on the new group to set the rules
- We could add a new rule, but instead...
- `Pin node`  under Certname and add "learning.puppetlabs.vm"
- In case the certname doesn't autofill run `puppet agent -t`
- *Make sure to click* `Commit 1 change`

### Add a class

`puppet module install ...` makes the module available for use in the console

To add class
- Click `Classes` tab
- find the `Class name` text box
  - begin typing `graphite`
  - *Note* if it doesn't autofill, hit `refresh` button near top right
- Click `Add Class`
- Set the following parameters
  - gr_web_server = none
  - gr_django_pkg = django
  - gr_django_provider = pip
  - gr_django_ver = "1.5"
- Click on `Add parameter` button for all parameters
- `Commit 5 changes`

### Run Puppet

Puppet daemon defaults to 30 mins runs.

To trigger immediately
    puppet agent --test

To test it installed correctly,

    http://IPADDRESS:90/render/?width=586&height=308&_salt=1430506380.148&from=-30minutes&fontItalic=false&fontName=Courier&target=alias(carbon.agents.learning_puppetlabs_vm-a.cpuUsage%2C"CPU")&target=alias(secondYAxis(carbon.agents.learning_puppetlabs_vm-a.memUsage)%2C"Memory")&majorGridLineColor=C0C0C0&minorGridLineColor=C0C0C0

## Resources


### Quest objectives

- Understand how *resources* on the system are modeled in Puppet's Domain
  Specific Language (*DSL*).
- Use Puppet to inspect *resources* on your system.
- Use the `Puppet Apply` tool to make changes to resources on your system.
- Learn about the Resource Abstraction Layer (*RAL*).

### Getting Started

    quest begin resources

### Resources

*Resource* := Puppets interpretion of any aspect of your system configuration
you want to manage (users, files, services, and packages, to give some common
examples) as a unit.

*Resource Declaration* := The block of code that describes a resource

### Puppet's Domain Specific Language

Puppet DSL is a **declarative language** := means that instead of defining a
process or set of commands, Puppet code describes (or declares) only the
desired end state.

    puppet resource user root

Should see something like:

```ruby
user { 'root':
  ensure           => present,
  comment          => 'root',
  gid              => '0',
  home             => '/root',
  password         => '$1$jrm5tnjw$h8JJ9mCZLmJvIxvDLjw1M/',
  password_max_age => '99999',
  password_min_age => '0',
  shell            => '/bin/bash',
  uid              => '0',
}
```

Resource declaration has *3 main components*
- Type
- Title
- Attribute value pairs

### Resource Type

    user { 'root':
      ...
    }

`user` is the *resource type*

Some common core resource types:
- user A user
- group A user group
- file A specific file
- package A software package
- service A running service
- cron A scheduled cron job
- exec An external command
- host A host entry

[Type Reference Document](http://docs.puppetlabs.com/references/latest/type.html)

### Resource Title


    user { 'root':
      ...
    }

`root` is the *resource title*

### Attribute Value Pairs

    user { 'root':
      ensure           => present,
      comment          => 'root',
      ...
    }

Hash of *attributes* and corresponding *values*

    puppet describe user | less

### Puppet Apply

    puppet apply -e "user { 'galatea': ensure => present, }"

    puppet resource user galatea

Use `-e` to drop output into a text editor

    puppet resource -e user galatea

This will open into a text editor you can edit and save to apply. e.g. add the following line in the editor

    comment => 'Galatea of Cyprus',

### Review

    puppet describe

    puppet resource

    puppet apply

    puppet resource

## Manifests and Classes

### Objectives

- Understand the concept of a Puppet manifest
- Construct and apply manifests to manage resources
- Understand what a class means in Puppet's Language
- Learn how to use a class definition
- Understand the difference between defining and declaring a class

### Getting started

    quest begin manifests_and_classes

### Defining Manifests & Classes

*manifest :=* puppet code saved to a file with the `.pp` extension

*Class :=*  named block of Puppet code
- next level of abstraction above resource
- declares a set of resources related to a single system component

### cowsay

`cd` to *modulepath*

    cd /etc/puppetlabs/code/environments/production/modules

Create a `cowsay.pp` manifest
    vim cowsayings/manifests/cowsay.pp

```puppet
class cowsayings::cowsay {
  package { 'cowsay':
    ensure   => present,
    provider => 'gem',
  }
}
```

Validate the manifest

    puppet parser validate cowsayings/manifests/cowsay.pp

Note: the parser *returns nothing* if there are no errors

To apply this code, you can classify nodes in *node classifier*.

To test the manifest, include it in `examples`

    vim cowsayings/examples/cowsay.pp

```puppet
include cowsayings::cowsay
```

run it `--noop` to do a dry run

    puppet apply --noop cowsayings/examples/cowsay.pp

Since this is a gem being installed, you might have to manually `gem install --local --no-rdoc --no-ri /var/cache/rubygems/gems/cowsay-*.gem` or set up a *local rubygems mirror*

Run the manifest

    puppet apply ...

### Fortune

Cowsay can use fortune package ...

    vim cowsayings/manifests/fortune.pp

```puppet
class cowsayings::fortune {
  package { 'fortune-mod':
    ensure => present,
  }
}
```

    puppet parser validate ...

  vim cowsayings/examples/fortune.pp

  puppet apply --noop ...

  puppet apply ...

To verify it works run this a couple times:

    fortune | cowsay

### Modules (Scope)

`cowsayings::` => *scope* for the classes in this module

Default scope is in the *main class*

    vim cowsayings/manifests/init.pp

```puppet
class cowsayings {
  include cowsayings::cowsay
  include cowsayings::fortune
}
```

    Validate and --noop

Since both manifests have already been applied, to test your changes

    puppet resource package fortune-mod ensure=absent
    puppet resource package cowsay ensure=absent provider=gem

    vim cowsayings/examples/init.pp

```puppet
include cowsayings
```

## Modules

### Objectives

- Understand the purpose of Puppet modules
- Learn the module directory structure
- Write and test a simple module

### Getting Started

    quest begin modules

### The modulepath

    puppet master --configprint modulepath

will list several paths where puppet modules live. For the learning VM we will
add code to `/etc/puppetlabs/code/environments/production/modules`

### Module Structure

To see what modules are installed

    puppet module list

To see structure of modules in a path,

    tree -L 2 -d /etc/puppetlabs/code/environments/production/modules/

e.g.

    /etc/puppetlabs/code/environments/production/modules/
    ├── cowsayings
    │   ├── manifests
    │   └── examples
    └── graphite
        ├── manifests
            ├── spec
                └── templates

### Create Vimrc module

    cd /etc/puppetlabs/code/environments/production/modules

    mkdir vimrc

    mkdir vimrc/{manifests,examples,files}

### Managing files

Copy existing vimrc into the module

    cp ~/.vimrc vimrc/files/vimrc

Make a simple change e.g. `set number` to the file

```vimrc vimrc/files/vimrc
  ...
  set nu
  ...
```

```puppet vimrc/manifests/init.pp

class vimrc {
  file { '/root/.vimrc':
    ensure => file,
    source => 'puppet:///modules/vimrc/vimrc',
  }
}

```

Validate syntax

    puppet parser validate vimrc/manifests/init.pp

### Test the module

    vim vimrc/examples/init.pp

    include vimrc

Apply with `--noop`

To see that your line numbering settings have been applied, open a file with
Vim. You should see the number of each line listed to the left.

## NTP

### Quest Objectives

- Use the puppet module tool to find and install modules on the Puppet Forge
- Learn how you can use the site.pp manifest to classify nodes.
- Use class parameters to adjust variables in a class as you declare it.

### Getting Started

    quest begin ntp

### Package/File/Service

Before installing NTP module, check the current state of NTP **resources**

Check state of NTP **package**
    puppet resource package ntp

Check state of NTP **file**
    puppet resource file /etc/ntp.conf

Check state of NTP **service**
    puppet resource service ntpd

### Installation

    puppet module install puppetlabs-ntp

### Classification with the site.pp manifest

    vim /etc/puppetlabs/code/environments/production/manifests/site.pp

```puppet
node 'learning.puppetlabs.vm' {
    include ntp
}
```

    puppet parser validate ...

    puppet agent -t

Inspect the ntp resources again using above commands

### Class defaults and class parameters

    grep server /etc/ntp.conf

Instead of `include ntp` we can set variables in a **parameterized class** as it's declared

    ```puppet
    class { 'ntp':
      servers => [
        'nist-time-server.eoni.com',
        'nist1-lv.ustiming.org',
        'ntp-nist.ldsbc.edu'
      ]
    }
    ```
Don't forget to parser validate and trigger update

## MySQL

    quest begin mysql

:red_circle: Task 1: Install mysql module

    puppet module install puppetlabs-mysql

:red_circle: Task 2: classify this node with mysql server class

    vim /etc/puppetlabs/code/environmnets/production/manifests/site.pp

```puppet
node 'learning.puppetlabs.vm' {
  class { '::mysql::server':
    root_password    => 'strongpassword',
    override_options => {
      'mysqld' => { 'max_connections' => '1024' }
    },
  }
}
```

:red_circle: Task 3: validate syntax and trigger puppet run

    puppet parser validate

    puppet agent -t

You can use `mysql` to test it's installed and configured. Note: `\q` to exit
the mysql prompt

### Scope

To view what was installed with the module...

    tree -P "*.pp" /etc/puppetlabs/code/environments/production/modules/mysql/manifests/

So class `mysql::server` corresponds to
    `/etc/puppetlabs/code/environments/production/modules/mysql/manifests/server.pp`

and `mysql::server::account_security` corresponds to
    `/etc/puppetlabs/code/environments/production/modules/mysql/manifests/server/account_security.pp`

### Account Security

:red_circle: Task 4: Include security class

```puppet
node 'learning.puppetlabs.vm' {
  include ::mysql::server::account_security
  ...
}
```

Validate and run puppet

Note: output similar to below that removes the test db and default users

```puppet
Notice:
/Stage[main]/Mysql::Server::Account_security/Mysql_database[test]/ensure:
removed
Notice:
/Stage[main]/Mysql::Server::Account_security/Mysql_user[@localhost]/ensure:
removed
Notice:
/Stage[main]/Mysql::Server::Account_security/Mysql_user[root@127.0.0.1]/ensure:
removed
```

### Types and Providers

The Mysql module includes types and providers

**type :=** defines the interface for a resource; set of properties to define
deisred state for the resource and the **parameters** that tell Puppet how to
manager the resource.

**provider :=** does the heavy lifting to bering the system into line with the
state defined by a resource declaration.


### Database, user, grant:

:red_circle: Task 5:

```puppet
  # Create a db
  mysql_database { 'lvm':
    ensure  => present,
    charset => 'utf8',
  }

  # Create a user
  mysql_user { 'lvm_user@localhost':
    ensure => present,
  }

  # Grant priveleges
  mysql_grant { 'lvm_user@localhost/lvm.*':
    ensure     => present,
    options    => ['GRANT'],
    privileges => ['ALL'],
    table      => 'lvm.*',
    user       => 'lvm_user@localhost',
  }
```

Validate and apply

## Variables and Parameters

### Quest objectives

- Learn how to assign and evaluate variables in a manifest.
- Use the string interpolation syntax to mix variables into strings.
- Set variable values with class parameters.

### Getting Started

    quest begin variables_and_parameters

### Variables

    $myvariable = 'look, a string!'

Note:
- unlike resource declarations, variable assignments are **parse-order dependent**
- using an undefined variable assignes `undef` with no error
- can only assign a variable **once within a scope**

### Variable interpolation

variables can be inserted in strings

```puppet
file { "${doc_root}/index.html": }
```
### Manage web content with variables

:red_circle: Task 1: create web `manifests` and `examples`

    cd /etc/puppetlabs/code/environments/production/modules/

    mkdir -p web/{manifests,examples}

:red_circle: Task 2: create web manifest

    vi web/manifests/init.pp

```puppet
class web {

  $doc_root = '/var/www/quest'

  $english = 'Hello world!'
  $french  = 'Bonjour le monde!'

  file { "${doc_root}/hello.html":
    ensure  => file,
    content => "<em>${english}</em>",
  }

  file { "${doc_root}/bonjour.html":
    ensure  => file,
    content => "<em>${french}</em>",
  }
}
```

:red_circle: Task 3: validate

    puppet parser

:red_circle: Task 4: apply using `--noop` first

    puppet apply --noop web/examples/init.pp

If it looks good

    puppet apply web/examples/init.pp

### Class Parameters

*Class Parameters :==* set a variable within the class as it's declared

To declare with **default value**

```puppet
 class classname ( $parameter = 'default' ) {
     ...
 }
```

To override
```puppet
 class {'classname':
   parameter => 'value',
 }
```

:red_circle: Task 5: Create and use class parameters

Rewrite web class with parameters

```puppet
 class web ( $page_name, $message ) {
```

Use the variables set by parameters

```puppet
 file { "${doc_root}/${page_name}.html":
   ensure  => file,
   content => "<em>${message}</em>",
 }
```

:red_circle: Task 6

```puppet
class { 'web':
  page_name => 'hola',
  message   => 'Hola mundo!',
}

```

:red_circle: Task 7 - run --noop and apply

Test at `<VM'S IP>/hola.html`


### Review

Using variables. You learned how to:
- assign a value to a variable
- reference the variable by name
- learned how to interpolate variables
- add parameters to a class.

## Conditional statements

### Quest objectives

- Learn how to use conditional logic to make your manifests adaptable.
- `if`, `unless`, `case`, and `selector` statements.

### Getting started

To start this quest enter the following command:

    quest begin conditional_statements

### Writing for flexibility

Puppet's DSL gives you the tools to build adaptability into your modules.

*Facts and conditional statements* are the bread and butter of this functionality.

### Facts

To get a full list of facts available to facter, enter the command:

    facter -p | less

You can reference any of the facts  with the same syntax you would use for a variable you had assigned within your manifest.

Facter facts exist in *top scope*
- Can be overwritten in lower scope
- Use `::` to explicitly scope references to facts

```puppet
$::factname
```

### Conditions

- if statements,
- unless statements,
- case statements, and
- selectors

### If

    cd /etc/puppetlabs/code/environments/production/modules

:red_circle: Task 1: Create an accounts directory and your examples and manifests directories:

    mkdir -p accounts/{manifests,examples}

:red_circle: Task 2: Open the accounts/manifests/init.pp manifest in Vim.

```puppet
class accounts ($user_name) {

  if $::operatingsystem == 'centos' {
    $groups = 'wheel'
  }
  elsif $::operatingsystem == 'debian' {
    $groups = 'admin'
  }
  else {
    fail( "This module doesn't support ${::operatingsystem}." )
  }

  notice ( "Groups for user ${user_name} set to ${groups}" )
}
```

*Note* that the string matches are *not case sensitive*,
- 'CENTOS' would work just as well as 'centos'.

Create a user resource declaration.

```puppet
class accounts ($user_name) {

  ...

  user { $user_name:
    ensure => present,
    home   => "/home/${user_name}",
    groups => $groups,
  }

}
```

`puppet parser validate`

:red_circle: Task 3: Create a test manifest (accounts/examples/init.pp) and declare
the accounts manifest with the name parameter set to dana.

```puppet
class {'accounts':
  user_name => 'dana',
}
```

:red_circle: Task 4: Test a different OS by overriding Facter's OS

    FACTER_operatingsystem=Debian puppet apply --noop accounts/examples/init.pp

Look in the list of notices, and you'll see the changes that would have been applied.

:red_circle: Task 5:

Try one more time with an unsupported operating system to check the fail condition:

    FACTER_operatingsystem=Darwin puppet apply --noop accounts/examples/init.pp

:red_circle: Task 6:

`puppet apply --noop` on your test manifest without setting the environment variable.

If this looks good, drop the --noop flag to apply the catalog generated from your manifest.

You can use the puppet resource tool to verify the results.

### Unless

The unless statement works like a reversed if statement.

### Case

Make sure to have a *default* clause

```puppet
case $::operatingsystem {
  'CentOS': { $apache_pkg = 'httpd' }
  'Redhat': { $apache_pkg = 'httpd' }
  'Debian': { $apache_pkg = 'apache2' }
  'Ubuntu': { $apache_pkg = 'apache2' }
  default: { fail("Unrecognized operating system for webserver.") }
}

package { $apache_pkg :
  ensure => present,
}
```

### Selector

Selector statements are similar to case statements, but instead of executing a
block of code, a selector *assigns a value directly*.

```puppet
$rootgroup = $::osfamily ? {
  'Solaris' => 'wheel',
  'Darwin'  => 'wheel',
  'FreeBSD' => 'wheel',
  'default' => 'root',
}
```

Because a selector can only return a value and cannot execute a function like
fail() or warning(), it is up to you to make sure your code *handles unexpected
conditions gracefully*.

## Resource Ordering

### Quest objectives

- Understand why some resources must be managed in a specific order.
- Use the `before`, `require`, `notify`, and `subscribe` metaparameters to specify order

### Getting started

This quest will help you learn more about specifying the order in which Puppet should manage resources in a manifest. When you're ready to get started, type the following command:

    quest begin resource_ordering

### Resource order

Puppet's **resource relationship** syntax lets you explicitly define the
dependency relationships among your resources.

**relationship metaparameters :=** a kind of attribute value pair that tells
Puppet how you want it to implement a resource, rather than the details of the
resource itself.

Relationship metaparameters are set in a resource declaration along with the
rest of a resource's attribute value pairs.

### before and require

`before` specifies *this* resource is executed first

```puppet
package { 'openssh-server':
  ensure => present,
  before => Service['sshd'],
}
```

**require** specified *other* resource should execute first

```puppet
service { 'sshd':
  ensure   => running,
  enable   => true,
  require  => Package['openssh-server'],
}
```

In both of these cases, take note of the way you refer to the target resource.
The **target's type is capitalized**, and **followed by an array**

    Type['title']

:red_circle: Task 1: create sshd directory

    cd /etc/puppetlabs/code/environments/production/modules
    mkdir -p sshd/{examples,manifests,files}

:red_circle: Task 2:
- Create an sshd/manifests/init.pp manifest and fill in your sshd class with
  the openssh-server package resource and sshd service resource.
- Don't forget to include a require or before to specify the relationship
  between these two resources. (If you need a hint, feel free to refer back to
  the examples above!)
- When you're done, use the puppet parser validate command to check your
  manifest.

When Puppet compiles a catalog, it generates a **graph that represents the network of resource relationships in that catalog**.

:red_circle: Task 3:
- set up an sshd/examples/init.pp manifest.

    include sshd

- run a test manifest with the --noop and --graph flags.

    puppet apply sshd/examples/init.pp --noop --graph

:red_circle: Task 4:

Puppet outputs a .dot file. You can find the graphdir location with

    puppet config print graphdir

Convert `.dot` to `.png`

    dot -Tpng /opt/puppetlabs/puppet/cache/state/graphs/relationships.dot -o \
    /var/www/quest/relationships.png

Take a look at `<VM'S IP>/relationships.png`.

:red_circle: Task 5:

Use a file resource to manage the sshd configuration. You can copy the existing
configuration file into your module's files.

    cp /etc/ssh/sshd_config sshd/files/sshd_config

ensure that the pe-puppet user has permissions to read this file.

    chown pe-puppet:pe-puppet sshd/files/sshd_config

:red_circle: Task 6:

    vi sshd/files/sshd_config file

and

    find the GSSAPIAuthentication line. Change the setting to no

:red_circle: Task 7:

Create file resource and ensure it is applied after `Package`

```puppet
class sshd {

  ...

  file { '/etc/ssh/sshd_config':
    ensure  => present,
    source  => 'puppet:///modules/sshd/sshd_config',
    require => Package['openssh-server'],
  }
}

```

:red_circle: Task 8:

Apply your test manifest again with the --graph and --noop flags, then use the
dot tool again to regenerate your graph image.

    dot -Tpng /opt/puppetlabs/puppet/cache/state/graphs/relationships.dot -o /var/www/quest/relationships.png

Check `<VM'S IP>/relationships.png` again to see how your new file resource fits in.

**Note**: changing `Service` or `File` will not restart the service.

### notify and subscribe

The `notify` and `subscribe` metaparameters establish the same dependency
relationships as before and require, respectively, and **also trigger a
refresh** whenever Puppet makes a change to the dependency.

:red_circle: Task 9:

```puppet
class sshd {

  ...

  service { 'sshd':

  ...

    subscribe => File['/etc/ssh/sshd_config'],
  }
  ...
}
```

- Validate your syntax with the puppet parser tool.
- apply your test manifest with the --graph and --noop flags,
- use the dot tool again to regenerate your graph image again.
- Check `<VM'S IP>/relationships.png` one more time. Notice that the sshd
  resource now depends on the /etc/ssh/sshd_config file.
- drop the --noop flag to actually apply your changes.

Notice that the content of the config file has changed, followed by a notice
for the 'refresh' for the sshd service.

### Chaining arrows

The `->` (ordering arrow) operator causes the resource to the left to be
applied before the resource to the right.

The `~>` (notification arrow) operator causes the resource on the left to be
applied before the resource on the right, **and sends a refresh event**

**This generally isn't good practice.** It is easy to overlook chaining
arrows

### Autorequires

**Autorequires :=** are relationships between resources that Puppet can figure out for
itself.

e.g. a file resource should always come after a parent directory that contains it

Find these relationships in the type reference section of the Puppet Docs page,
as well as the output of the puppet describe tool.

    puppet describe user | less

Will include the following:

    **Autorequires:** If Puppet is managing the user's primary group (as
    provided in the `gid` attribute), the user resource will autorequire that
    group. If Puppet is managing any role accounts corresponding to the user's
    roles, the user resource will autorequire those role accounts.

### Review

- specify relationships between resources.
- `--graph` flag and `dot` tool to visualize relationships
- `notify` and `subscribe` to refresh a service
- chaining arrows
- autorequires

## Defined Resource Types

### Quest objectives

- Understand how to manage multiple groups of resources with defined resource
  types.
- Use a defined resource type to easily create home pages for users.

### Getting Started

**Defined resource type :=** block of Puppet code that can be declared multiple times with different parameter values.

In this quest, you will create a defined resource type for a web_user. This
will let you bundle together the resources you need to create a user along with
their personal web homepage. This way you can handle everything with a single
resource declaration.

    quest begin defined_resource_types

### Defined resource types

Writing custom providers, however, is a significant commitment. When you start
writing your own providers, you're taking on responsibility for all the
abstraction Puppet uses to handle the implementation of that resource on
diverse operating systems and configurations. Though this kind of project can
be a great contribution to the Puppet community, it's not generally appropriate
for a one-off solution.

Puppet's *defined resource types* are a **lightweight alternative** to
*Customer Providers*

:red_circle: Task 1:

- create module structure for `web_user` module

    cd /etc/puppetlabs/code/environments/production/modules

- create the directories for your new module

    mkdir -p web_user/{manifests,examples}

:red_circle: Task 2:

Go ahead and create a user.pp manifest where we'll define our defined resource type:

    vim web_user/manifests/user.pp

```puppet
define web_user::user {

  $home_dir = "/home/${title}"

  user { $title:
    ensure => present,
  }

  file { $home_dir:
    ensure  => directory,
    owner   => $title,
    group   => $title,
    mode    => '0775',
  }
}
```

**Note** the use of `define` keyword instead of class

- *defined resource type can be realized multiple times* on a single system
- vs *classes are always singleton*.

Also **note** the use of `$title` even though it hasn't been explicitly assigned

:red_circle: Task 3:

Create example

    vim web_user/examples/user.pp

Declare a web_user::user resource

    web_user::user { 'shelob': }

The title `shelob` is passed through to our defined resource type as the `$title`
variable.

:red_circle: Task 4:

- run a --noop
- apply your test manifest

    puppet apply web_user/examples/user.pp

Now take a look at the /home directory:

    ls -la /home

You should now see a home directory for shelob with the permissions you specified:

    drwxr-xr-x   4 shelob    shelob    4096 Nov  4 18:20 shelob

### Public HTML homepages

Here's an example of real usage of defined resource type. The Quest guide
manifests includes the following code that sets any user's directory with
`/home/<user>/index.html` to serve that as a page at
`/home/username/public_html/index.html`

```puppet

nginx::resource::location { '~ ^/~(.+?)(/.*)?$':
  vhost          => '_',
  location_alias => '/home/$1/public_html$2',
  autoindex      => true,
}

```

To view the result of this defined resource type...

    cat /etc/nginx/sites-enabled/_.conf

:red_circle: Task 5:

- Give web_user::user resource a public_html directory and a default index.html page
- add a directory and file
- replace parameter for index.html to false - create file if it doesn't exist
- string interpolation to customize the default content

Reopen your manifest:

    vim web_user/manifests/user.pp

And add code to configure your user's public_html directory and default index.html file:

```puppet

define web_user::user {

  $home_dir    = "/home/${title}"
  $public_html = "${home_dir}/public_html"

  user { $title:
    ensure     => present,
  }

  file { [$home_dir, $public_html]:
    ensure  => directory,
    owner   => $title,
    group   => $title,
    mode    => '0775',
  }

  file { "${public_html}/index.html":
    ensure  => file,
    owner   => $title,
    group   => $title,
    replace => false,
    content => "<h1>Welcome to ${title}'s home page!</h1>",
    mode    => '0664',
  }
}

```

:red_circle: Task 6:

- puppet parser validate tool to check your manifest
- run a --noop before applying your test manifest again

    puppet apply web_user/examples/user.pp

- Take a look at your user's new default at `<VM'S IP>/~shelob/index.html`

### Parameters

By default defined resource types only allow you to specify the `title`

We can pass additional information via **parameters**

:red_circle: Task 7:

```puppet

  define web_user::user (

    $content  = "<h1>Welcome to ${title}'s home page!</h1>",
    $password = undef,

  ) {
```

**Note** `$password = undef` since parameters must have a default value

```puppet

define web_user::user (

  $content  = "<h1>Welcome to ${title}'s home page!</h1>",
  $password = undef,

) {

  $home_dir    = "/home/${title}"
  $public_html = "${home_dir}/public_html"

  user { $title:
    ensure   => present,
    password => $password,
  }

  file { [$home_dir, $public_html]:
    ensure => directory,
    owner  => $title,
    group  => $title,
    mode    => '0775',
  }

  file { "${public_html}/index.html":
    ensure  => file,
    owner   => $title,
    group   => $title,
    replace => false,
    content => $content,
    mode    => '0664',
  }
}
```

:red_circle: Task 8:

Edit your test manifest, and add a new user to try this out:

```puppet

web_user::user { 'shelob': }

web_user::user { 'frodo':
  content  => 'Custom Content!',
  password => pw_hash('sting', 'SHA-512', 'mysalt'),
}

```

**Note** using the `pw_hash` function to generate a SHA-512 hash

:red_circle: Task 9:

- --noop run
- apply your test manifest

    puppet apply web_user/examples/user.pp

- check your new user's page at `<VM'S IP>/~frodo/index.html`

### Review

- introduced defined resource types
- Defined resource type definitions use similar syntax to class declarations,
  use the `define` keyword instead of class.
- Use the `$title` variable in constituent resource titles to ensure uniqueness.
- Resource with no parameters can be declared in short `{'title': }` form
- you cannot use the *value of one parameter to set another*
- The exception to above is the $title variable.
- Parameters without a default value are required
- You can use the `undef` value as a default

## Agent Node Setup

### Quest objectives

- Learn how to *install the Puppet agent* on a node.
- Use the PE console to *sign the certificate* of a new node.
- Understand a *simple Puppet architecture* with a Puppet master serving multiple agent nodes.
- Use the *site.pp* manifest to classify nodes.

### Getting Started

Use a tool called docker to simulate multiple nodes

    quest begin agent_setup

### Get Some Nodes

`puppet apply` compiles a catalog based on a specified manifest and applies that
catalog locally.

`puppet agent -t` triggers a Puppet run.
- *agent sends* a collection of **facts** to the Puppet master.
- *master takes* these facts and uses them to determine what **Puppet code**
  should be applied
- two ways that this *classification can be configured*: the `site.pp` manifest
  and the `PE console` node classifier.
- *master evaluates* the Puppet code to **compile a catalog**
- *master sends* that **catalog** to the agent on the node
- *agent applies* **catalog**
- *agent sends* its **report** of the Puppet run back to the master

### Containers

*We've created* a `multi_node` module that will set up a pair of docker
containers to act as additional agent nodes in your infrastructure.

:red_circle: Task 1: Apply the `multi_node` class to the learning VM

    vim /etc/puppetlabs/code/environments/production/manifests/site.pp

```puppet
node learning.puppetlabs.vm {
    include multi_node
      ...
}
```

:exclamation: it's important that you don't put this in your default node
declaration. If you did, Puppet would try to create docker containers on your
docker containers every time you did a Puppet run!

:red_circle: Task 2: Trigger an agent run

    puppet agent -t

Once this run has completed, you can use the `docker ps` command to see your two
new nodes. You should see one called database and one called webserver.

### Install the Puppet agent

Now you have two fresh nodes, but you don't have the Puppet agent installed on either!

:red_circle: Task 3: Classify `pe_repo::platform::ubuntu...`

If Master & Agent OS are the same...
`curl -k https://<PUPPET MASTER HOSTNAME>:8140/packages/current/install.bash | sudo bash`

Otherwise...

Navigate to `https://<VM's IP address>` in your browser address bar. Use the
following credentials to connect to the console:
- username: admin
- password: puppetlabs

In the `Nodes > Classification` section
- click on the PE Master node group.
- Under the Classes tab, enter pe_repo::platform::ubuntu_1404_amd64.
- Click the Add class button
- commit the change.

    puppet agent -t

:red_circle: Task 4: Install Puppet Agent on agent nodes

    docker exec -it webserver bash

Paste in the curl command from the PE console (below) to install the Puppet
agent on the node

:exclamation: For future reference, you can find the curl command needed to
install the Puppet agent in the `Nodes > Unsigned Certificates` section of the
PE console)

    curl -k https://learning.puppetlabs.vm:8140/packages/current/install.bash | sudo bash

:exclamation: The installation may take several minutes. (If you encounter an
error at this point, you may need to *restart your Puppet master service*:
`service pe-puppetserver restart`) When it completes, end your bash process on
the container:

    exit

repeat the process with your database node:

    docker exec -it database bash

Now you have two new nodes with the Puppet agent installed.

Let's use facter to get some information about this node:

    facter operatingsystem

    facter fqdn

:red_circle: Task 5: Test agent is working

    puppet resource file /tmp/test ensure=file

    vim /tmp/test.pp

```puppet
notify { "Hi, I'm a manifest applied locally on an agent node": }
```

    puppet apply /tmp/test.pp

You should see the puppet output with the notice

Since this is an agent node, you'll notice there are no `modules` or `site.pp`
manifests in `ls /etc/puppetlabs/code/environments/production/manifests` and
`ls /etc/puppetlabs/code/environments/production/modules`

:warning: Unless you're doing local development and testing of a module, all
the Puppet code for your infrastructure is kept on the Puppet master node, not
on each individual agent.

When a Puppet run is triggered—either as scheduled or manually with the puppet
agent -t command, the Puppet master compiles your Puppet code into a catalog
and sends it back to the agent to be applied.

    puppet agent -t

You'll see that instead of completing a Puppet run, Puppet exits with the following message:

    Exiting; no certificate found and waitforcert is disabled


### Certificates

Before you can run Puppet on your new agent nodes, you need to sign their
certificates on the Puppet master.

    If you're still connected to your agent node, return to the master

:red_circle: Task 6: Use the puppet cert list command to list the unsigned certificates.

(You can also view and sign these from the inventory page of the PE console.)

    puppet cert list

    puppet cert sign webserver.learning.puppetlabs.vm

    puppet cert sign database.learning.puppetlabs.vm

:red_circle: Task 7: Now your certificates are signed, so your new nodes can be managed by Puppet. To test this out, let's add a simple notify resource to the site.pp manifest on the master.

    vim /etc/puppetlabs/code/environments/production/manifests/site.pp

```puppet
node default {
    notify { "This is ${::fqdn}, running the ${::operatingsystem} operating system": }
}
```

Now connect to our database node again.

    docker exec -it database bash

And try another Puppet run:

    puppet agent -t

With your certificate signed, the agent on your node was able to properly
request a catalog from the master and apply it to complete the Puppet run.

### Review

- Reviewed the difference between using puppet apply to locally compile and
  apply a manifest and using the puppet agent -t command to trigger a Puppet
  run.
- Created two new nodes, and explored the similarities and differences in
  Puppet on the agent and master.
- To get the Puppet master to recognize the nodes, you used the puppet cert
  command to sign their certificates.
- Used a `notify` resource in the `default` node definition of your `site.pp`
  manifest and triggered a Puppet run on an agent node to see its effect.

DONE

## Application Orchestrator

### Quest objectives

- Understand the role of orchestration
- Configure the Puppet Application Orchestration service
- Configure the Orchestrator client.
- Define components and compose them into an application stack.
- Use `puppet job run` command across a group of nodes.

### Getting Started

If you manage applications comprised of multiple services distributed across
multiple nodes, you'll know that the orchestration of multiple nodes can pose
some special challenges.

Your applications likely need to
- share information among the nodes
- make configuration changes in the right order

Puppet's Application Orchestrator extends Puppet's powerful declarative model
from the level of the single node to that of the complex application.

    quest begin application_orchestrator

### Application orchestrator

Imagine a simple two tier web application with a load balancer.

                                database.example.com
                                        ^
                                        ^
             > > > > > > > > > > > > > >^< < < < < < < < < < < < <
            ^                           ^                         ^
            ^                           ^                         ^
    webserver01.example.com    webserver02.example.com    webserver03.example.com
            ^                           ^                         ^
            ^                           ^                         ^
            < < < < < < < < < < < < < < ^ > > > > > > > > > > > > >
                                        ^
                                        ^
                                  lb.example.com

We have a single load balancer that distributes requests among three
webservers, which all connect to the same database server.
- Some components e.g. sshd, ntp will be common to many nodes
- Some code will be application specific, e.g. db, app


                            |-- ntp
                            |-- sshd
    database.example.com << |-- mysql::server
                            |-- mysql::bindings
                            |-- mysql::db

This application specific configuration is called a *component*.

In our example, we define components for the database, webserver, and
loadbalancer.

    ------------      -------------    ----------------
    | database |      | webserver |    | loadbalancer |
    ------------      -------------    ----------------
        ^                  ^                 ^
        |                  |                 |
    database.pp       webserver.pp     loadbalancer.pp

```puppet
    # example database.pp

    define {'database':
      mysql::server
      mysql::bindings
      mysql::db
    }
```

With all the components defined, we next define their *relationships* with one
another as an application.

If your application is packaged as a module, this application definition will
generally go in your `init.pp` manifest.

The application definition
- tells apps how they'll communicate with one another
- allows the Puppet Application Orchestrator to determine the order of Puppet
  runs needed

The power of Orchestrator is in determining the order of puppet runs so that
e.g. if the Web Server is dependant on DB then make sure that the DB is up and
running before configuring the server.

### Node Configuration

To coordinate changes,
- set the nodes to use a *cached catalog*.
- *disable plugin sync*

:red_circle: Task 1: Edit *ini setting* resource to apply globally to all nodes

    vim /etc/puppetlabs/code/environments/production/manifests/site.pp

    ```puppet
    node /^(webserver|database).*$/ {
      pe_ini_setting { 'use_cached_catalog':
        ensure  => present,
        path    => $settings::config,
        section => 'agent',
        setting => 'use_cached_catalog',
        value   => 'true',
      }
      pe_ini_setting { 'pluginsync':
        ensure  => present,
        path    => $settings::config,
        section => 'agent',
        setting => 'pluginsync',
        value   => 'false',
      }
    }
    ```

:red_circle: Task 2: Trigger Puppet runs on the two nodes directly from the PE console.
- `https://<VM'S IP ADDRESS>`
  - User: admin
  - Password: puppetlabs
- Go to the Nodes > Inventory section in the PE console.
- Click on your database.learning.puppetlabs.vm node
- click on the Run Puppet... button link and Run button to start your Puppet
  run.
- Return to the Inventory section and trigger a run on
  webserver.learning.puppetlabs.vm as well

### Master Configuration

We need additional steps on Master to get Puppet Application Orchestrator
configured.

### Client Configuration and Permissions

We can use *client tools* to run puppet from our local workstation.

:red_circle: Task 3:

    mkdir -p ~/.puppetlabs/client-tools

Now create your orchestrator configuration file.

    vim ~/.puppetlabs/client-tools/orchestrator.conf

```json
{
  "options": {
    "url": "https://learning.puppetlabs.vm:8143",
    "environment": "production"
  }
}
```

Set *RBAC* permissions to allow interaction.
- Return to the PE console and find the Access control section in the left
  navigation bar.
- Click on the Users section of the navigation bar.
- Add a new user with the full name "Orchestrator" and login "orchestrator".
- Click on the user's name to see its details
- click the "Generate password reset" link.
- Copy and paste the url provided into your browser address bar
- Set the user's password to "puppet"

Next, we need to give this new user permissions to run the Puppet Orchestrator.
- Go to the User Roles section
- create a new role with the name "Orchestrators" and description "Run the Puppet Orchestrator."
- Once this new role is created, click on its name to modify it.
- Select your "Orchestrator" user from the drop-down and add it to the role.
- Finally, go to the Permissions tab.
- Select "Puppet agent" from the Type drop-down
- "Run Puppet form Orchestrator" from the Permission drop-down.
- Click Add permission.

### Client token

We can now generate an *RBAC access token* to authenticate to the
*Orchestration service*

:red_circle: Task 4:

`--lifetime=1d` sets expiry on the token

    puppet access login --service-url https://learning.puppetlabs.vm:4433/rbac-api --lifetime=1y

### Puppetized Applications

Application definition is packaged in a Puppet module. For this exercise we
will build a LAMP stack.

    | -------------------------------- |
    | webserver.learning.puppetlabs.vm |
    | -------------------------------- |
                  |
                  V
    | ------------------------------- |
    | database.learning.puppetlabs.vm |
    | ------------------------------- |

Install required modules

    puppet module install puppetlabs-mysql

    puppet module install puppetlabs-apache

Requirements for orchestration:
- make sure nodes are deployed in correct order
- pass information among nodes

Webserver needs to know hostname, db name, user, password to connect.

In order to pass info from database to webserver, the database will create a
*custom resource* named sql.

:red_circle: Task 5:

    cd /etc/puppetlabs/code/environments/production/modules

    mkdir -p lamp/{manifests,lib/puppet/type}

The lib/puppet/ directory is where you keep any *extensions* to the core Puppet
language that your module provides.

For example, in addition to types, you might also define new providers or functions.

:red_circle: Task 6:

Now let's go ahead and create our new sql resource type.

    vim lamp/lib/puppet/type/sql.rb

The new type is defined by a block of Ruby code, like so:

```ruby
Puppet::Type.newtype :sql, :is_capability => true do
  newparam :name, :is_namevar => true
  newparam :user
  newparam :password
  newparam :host
  newparam :database
end
```

*Note* that it's the `is_capability => true` bit that lets this resource live
on the *environment level*, rather than being applied to a specific node.

:red_circle: Task 7:

    vim lamp/manifests/mysql.pp

It will look like this:

```puppet
define lamp::mysql (
  $db_user,
  $db_password,
  $host     = $::hostname,
  $database = $name,
) {

  class { '::mysql::server':
    service_provider => 'debian',
    override_options => {
      'mysqld' => { 'bind-address' => '0.0.0.0' }
    },
  }

  mysql::db { $name:
    user     => $db_user,
    password => $db_password,
    host     => '%',
    grant    => ['SELECT', 'INSERT', 'UPDATE', 'DELETE'],
  }

  class { '::mysql::bindings':
    php_enable       => true,
    php_package_name => 'php5-mysql',
  }

}
Lamp::Mysql produces Sql {
  user     => $db_user,
  password => $db_password,
  host     => $host,
  database => $database,
}
```

Because orchestration uses some new syntax, include the `--app_management` flag
when validating.

    puppet parser validate --app_management lamp/manifests/mysql.pp

:red_circle: Task 8:

Next, create a webapp component to configure an Apache server and a simple PHP application:

    vim lamp/manifests/webapp.pp

It will look like this:

```puppet
define lamp::webapp (
  $db_user,
  $db_password,
  $db_host,
  $db_name,
  $docroot = '/var/www/html'
) {
  class { 'apache':
    default_mods  => false,
    mpm_module    => 'prefork',
    default_vhost => false,
  }

  apache::vhost { $name:
    port           => '80',
    docroot        => $docroot,
    directoryindex => ['index.php','index.html'],
  }

  package { 'php5-mysql':
    ensure => installed,
    notify => Service['httpd'],
  }

  include apache::mod::php

  $indexphp = @("EOT"/)
    <?php
    \$conn = mysql_connect('${db_host}', '${db_user}', '${db_password}');
    if (!\$conn) {
      echo 'Connection to ${db_host} as ${db_user} failed';
    } else {
      echo 'Connected successfully to ${db_host} as ${db_user}';
    }
    ?>
    | EOT

  file { "${docroot}/index.php":
    ensure  => file,
    content => $indexphp,
  }

}
Lamp::Webapp consumes Sql {
  db_user     => $user,
  db_password => $password,
  db_host     => $host,
  db_name     => $database,
}
```

    puppet parser validate --app_management lamp/manifests/webapp.pp

:red_circle: Task 9:

Now that we have all of our components ready to go, we can define the application itself.

    vim lamp/manifests/init.pp

```puppet
application lamp (
  $db_user,
  $db_password,
) {

  lamp::mysql { $name:
    db_user     => $db_user,
    db_password => $db_password,
    export      => Sql[$name],
  }

  lamp::webapp { $name:
    consume => Sql[$name],
  }

}
```


Note the use of

    Lamp::Mysql produces Sql { ...

    Lamp::Webapp consumes Sql { ...

Validate

    puppet parser validate --app_management lamp/manifests/init.pp

Verify all the components are in place

    tree lamp

Your module should look like the following:

    modules/lamp/
    ├── lib
    │   └── puppet
    │       └── type
    │           └── sql.rb
    └── manifests
        ├── init.pp
        ├── mysql.pp
        └── webapp.pp

    4 directories, 4 files

:red_circle: Task 10:

Now that your application is defined, the final step is to
Declare your application in site.pp

    vim /etc/puppetlabs/code/environments/production/manifests/site.pp

Until now, most of the configuration you've made in your site.pp has been in the context of node blocks. An application, however, is applied to your environment independently of any classification defined in your node blocks or the PE console node classifier. To express this distinction, we

Declare our application instance in a *special block* called `site` as distinct from a node block.

```puppet
site {
  lamp { 'app1':
    db_user     => 'roland',
    db_password => '12345',
    nodes       => {
      Node['database.learning.puppetlabs.vm']  => Lamp::Mysql['app1'],
      Node['webserver.learning.puppetlabs.vm'] => Lamp::Webapp['app1'],
    }
  }
}
```

*Note* the `Node` parameter is where the orchestration magic happens.

Use the `puppet app` tool to view the application.

    puppet app show

You should see a result like the following:

    Lamp['app1']
      Lamp::Mysql['app1'] => database.learning.puppetlabs.vm
          - produces Sql['app1']
      Lamp::Webapp['app1'] => webserver.learning.puppetlabs.vm
          - consumes Sql['app1']

:red_circle: Task 11:

Use the `puppet job` command to deploy the application.

    puppet job run Lamp['app1']

You can check on the status of any running or completed jobs with the `puppet job list` command.

Log in to the database server and have a look our MySQL instance.

    docker exec -it database bash

    puppet resource service mysql

Now go ahead and disconnect from the database node.

    exit

go to `http://<IP_ADDRESS>:10080/index.php` to see your PHP website.

### Review

`Puppet Orchestrator` tool to coordinate Puppet runs across multiple nodes.

View the docs at [PE
Orchestration](https://docs.puppet.com/pe/latest/app_orchestration_overview.html).

Defining an application generally requires several distinct manifests and ruby
extensions:
- *Application components*, which are typically written as *defined resource
  types*
- New *type definitions* for any environment resources needed to pass
  parameters among your components
- An *application definition* to declare your application components and
  specify their relationships to one another.
- A declaration of your application in the site block of your site.pp manifest
  to assign your components to *nodes* in your infrastructure.

Once an application is defined, you can use the `puppet app show` command to
see it, and the `puppet job run` command to run it. You can see running and
completed jobs with the `puppet job list` command.

## Next Steps

- [ ] [Roles & Profiles](https://docs.puppet.com/pe/latest/r_n_p_full_example.html)

- [ ] [Code Manager](http://www.evergreenitco.com/evergreenit-blog/2016/5/25/automate-puppet-code-deployments-with-code-manager)

# TOC

1. [1 Welcome](#1-welcome)
2. [2 The Power of Puppet](#2-the-power-of-puppet)
	1. [Get Started](#get-started)
	2. [Forge Ahead](#forge-ahead)
	3. [Class and Classification](#class-and-classification)
	4. [Create a Node Group](#create-a-node-group)
	5. [Add a class](#add-a-class)
	6. [Run Puppet](#run-puppet)
3. [3 Resources](#3-resources)
	1. [Quest objectives](#quest-objectives)
	2. [Getting Started](#getting-started)
	3. [Resources](#resources)
	4. [Puppet's Domain Specific Language](#puppet's-domain-specific-language)
	5. [Resource Type](#resource-type)
	6. [Resource Title](#resource-title)
	7. [Attribute Value Pairs](#attribute-value-pairs)
	8. [Puppet Apply](#puppet-apply)
	9. [Review](#review)
4. [4 Manifests and Classes](#4-manifests-and-classes)
	1. [Objectives](#objectives)
	2. [Getting started](#getting-started)
	3. [Defining Manifests & Classes](#defining-manifests-&-classes)
	4. [cowsay](#cowsay)
	5. [Fortune](#fortune)
	6. [Modules (Scope)](#modules-(scope))
5. [5 Modules](#5-modules)
	1. [Objectives](#objectives)
	2. [Getting Started](#getting-started)
	3. [The modulepath](#the-modulepath)
	4. [Module Structure](#module-structure)
	5. [Create Vimrc module](#create-vimrc-module)
	6. [Managing files](#managing-files)
	7. [Test the module](#test-the-module)
6. [6 NTP](#6-ntp)
	1. [Quest Objectives](#quest-objectives)
	2. [Getting Started](#getting-started)
	3. [Package/File/Service](#package/file/service)
	4. [Installation](#installation)
	5. [Classification with the site.pp manifest](#classification-with-the-site.pp-manifest)
	6. [Class defaults and class parameters](#class-defaults-and-class-parameters)
7. [7 MySQL](#7-mysql)
	1. [Scope](#scope)
	2. [Account Security](#account-security)
	3. [Types and Providers](#types-and-providers)
	4. [Database, user, grant:](#database,-user,-grant:)
8. [8 Variables and Parameters](#8-variables-and-parameters)
	1. [Quest objectives](#quest-objectives)
	2. [Getting Started](#getting-started)
	3. [Variables](#variables)
	4. [Variable interpolation](#variable-interpolation)
	5. [Manage web content with variables](#manage-web-content-with-variables)
	6. [Class Parameters](#class-parameters)
	7. [Review](#review)
9. [9 Conditional statements](#9-conditional-statements)
	1. [Quest objectives](#quest-objectives)
	2. [Getting started](#getting-started)
	3. [Writing for flexibility](#writing-for-flexibility)
	4. [Facts](#facts)
	5. [Conditions](#conditions)
	6. [If](#if)
	7. [Unless](#unless)
	8. [Case](#case)
	9. [Selector](#selector)
10. [10 Resource Ordering](#10-resource-ordering)
	1. [Quest objectives](#quest-objectives)
	2. [Getting started](#getting-started)
	3. [Resource order](#resource-order)
	4. [before and require](#before-and-require)
	5. [notify and subscribe](#notify-and-subscribe)
	6. [Chaining arrows](#chaining-arrows)
	7. [Autorequires](#autorequires)
	8. [Review](#review)
11. [11 Defined Resource Types](#11-defined-resource-types)
	1. [Quest objectives](#quest-objectives)
	2. [Getting Started](#getting-started)
	3. [Defined resource types](#defined-resource-types)
	4. [Public HTML homepages](#public-html-homepages)
	5. [Parameters](#parameters)
	6. [Review](#review)
12. [12 Agent Node Setup](#12-agent-node-setup)
	1. [Quest objectives](#quest-objectives)
	2. [Getting Started](#getting-started)
	3. [Get Some Nodes](#get-some-nodes)
	4. [Containers](#containers)
	5. [Install the Puppet agent](#install-the-puppet-agent)
	6. [Certificates](#certificates)
	7. [Review](#review)
13. [13 Application Orchestrator](#13-application-orchestrator)
	1. [Quest objectives](#quest-objectives)
	2. [Getting Started](#getting-started)
	3. [Application orchestrator](#application-orchestrator)
	4. [Node Configuration](#node-configuration)
	5. [Master Configuration](#master-configuration)
	6. [Client Configuration and Permissions](#client-configuration-and-permissions)
	7. [Client token](#client-token)
	8. [Puppetized Applications](#puppetized-applications)
	9. [Review](#review)
14. [Next Steps](#next-steps)

