# Keeping part of your Codebase private on Github 

https://24ways.org/2013/keeping-parts-of-your-codebase-private-on-github/

Open source is brilliant, theres no denying that, and GitHub
has been instrumental in open sources recent success. Im a
keen open-sourcerer myself, and I have a number of projects on
GitHub. However, as great as sharing code is, we often want to
keep some projects to ourselves. To this end, GitHub created
private repositories which act like any other Git repository,
only, well, private!

A slightly less common issue, and one Ive come up against
myself, is the desire to only keep certain parts of a codebase
private. A great example would be my site, CSS Wizardry; I
want the code to be open source so that people can poke
through and learn from it, but I want to keep any draft blog
posts private until they are ready to go live. Thankfully,
there is a very simple solution to this particular problem:
using multiple remotes.

Before we begin, its worth noting that you can actually build
a GitHub Pages site from a private repo. You can keep the
entire source private, but still have GitHub build and display
a full Pages/Jekyll site. I do this with csswizardry.net. This
post will deal with the more specific problem of keeping only
certain parts of the codebase (branches) private, and expose
parts of it as either an open source project, or a built
GitHub Pages site.

N.B. This post requires some basic Git knowledge.  

## Adding your public remote

Lets assume youre starting from scratch and you currently have
no repos set up for your project. (If you do already have your
public repo set up, skip to the "Adding your private remote"
section.)

So, we have a clean slate: nothing has been set up yet, were
doing all of that now. On GitHub, create two repositories. For
the sake of this article we shall call them site.com and
private.site.com. Make the site.com repo public, and the
private.site.com repo private (you will need a paid GitHub
account).

On your machine, create the site.com directory, in which your
project will live. Do your initial work in there, commit some
stuff  whatever you need to do. Now we need to link this local
Git repo on your machine with the public repo (remote) on
GitHub. We should all be used to this:

    $ git remote add origin git@github.com:[user]/site.com.git

Here we are simply telling Git to add a remote called origin
which lives at git@github.com:[user]/site.com.git. Simple
stuff. Now we need to push our current branch (which will be
master, unless youve explicitly changed it) to that remote:

    $ git push -u origin master

Here we are telling Git to push our master branch to a
corresponding master branch on the remote called origin, which
we just added. The -u sets upstream tracking, which basically
tells Git to always shuttle code on this branch between the
local master branch and the master branch on the origin
remote.  Without upstream tracking, you would have to tell Git
where to push code to (and pull it from) every time you ran
the push or pull commands. This sets up a permanent bond, if
you like.

This is really simple stuff, stuff that you will probably have
done a hundred times before as a Git user. Now to set up our
private remote.  

## Adding your private remote

Weve set up our public, open source repository on GitHub, and
linked that to the repository on our machine. All of this code
will be publicly viewable on GitHub.com. (Remember, GitHub is
just a host of regular Git repositories, which also puts a
nice GUI around it all.) We want to add the ability to keep
certain parts of the codebase private. What we do now is add
another remote repository to the same local repository. We
have two repos on GitHub (site.com and private.site.com), but
only one repository (and, therefore, one directory) on our
machine. Two GitHub repos, and one local one.

In your local repo, check out a new branch. For the sake of
this article we shall call the branch dev. This branch might
contain work in progress, or draft blog posts, or anything you
dont want to be made publicly viewable on GitHub.com. The
contents of this branch will, in a moment, live in our private
repository.

    $ git checkout -b dev

We have now made a new branch called dev off the branch we
were on last (master, unless you renamed it).

Now we need to add our private remote (private.site.com) so
that, in a second, we can send this branch to that remote:

    $ git remote add private git@github.com:[user]/private.site.com.git

Like before, we are just telling Git to add a new remote to
this repo, only this time weve called it private and it lives
at git@github.com:[user]/private.site.com.git. We now have one
local repo on our machine which has two remote repositories
associated with it.

Now we need to tell our dev branch to push to our private
remote:

    $ git push -u private dev

Here, as before, we are pushing some code to a repo. We are
saying that we want to push the dev branch to the private
remote, and, once again, weve set up upstream tracking. This
means that, by default, the dev branch will only push and pull
to and from the private remote (unless you ever explicitly
state otherwise).

Now you have two branches (master and dev respectively) that
push to two remotes (origin and private respectively) which
are public and private respectively.

Any work we do on the master branch will push and pull to and
from our publicly viewable remote, and any code on the dev
branch will push and pull from our private, hidden remote.  

## Adding more branches

So far weve only looked at two branches pushing to two
remotes, but this workflow can grow as much or as little as
youd like. Of course, youd never do all your work in only two
branches, so you might want to push any number of them to
either your public or private remotes. Lets imagine we want to
create a branch to try something out real quickly:

    $ git checkout -b test

Now, when we come to push this branch, we can choose which
remote we send it to:

    $ git push -u private test

This pushes the new test branch to our private remote (again,
setting the persistent tracking with -u).

You can have as many or as few remotes or branches as you
like.  

## Combining the two

Lets say youve been working on a new feature in private for a
few days, and youve kept that on the private remote. Youve now
finalised the addition and want to move it into your public
repo. This is just a simple merge. Check out your master
branch:

    $ git checkout master

Then merge in the branch that contained the feature:

    $ git merge dev

Now master contains the commits that were made on dev and,
once youve pushed master to its remote, those commits will be
viewable publicly on GitHub:

    $ git push

Note that we can just run $ git push on the master branch as
wed previously set up our upstream tracking (-u).  

## Multiple machines

So far this has covered working on just one machine; we had
two GitHub remotes and one local repository. Lets say youve
got yourself a new Mac (yay!) and you want to clone an
existing project:

    $ git clone git@github.com:[user]/site.com.git

This will not clone any information about the remotes you had
set up on the previous machine. Here you have a fresh clone of
the public project and you will need to add the private remote
to it again, as above.  

## Done!

If youd like to see me blitz through all that in one go, check
the showterm recording.

The beauty of this is that we can still share our code, but we
dont have to develop quite so openly all of the time. Building
a framework with a killer new feature? Keep it in a private
branch until its ready for merge. Have a blog post in a Jekyll
site that youre not ready to make live? Keep it in a private
drafts branch. Working on a new feature for your personal
site? Tuck it away until its finished. Need a staging area for
a Pages-powered site? Make a staging remote with its own
custom domain.

All this boils down to, really, is the fact that you can bring
multiple remotes together into one local codebase on your
machine. What you do with them is entirely up to you!
