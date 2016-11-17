# Git Tutorial

Used git, but only a little?
Want to know more about collaborating with other people?
Check out our git tutorial!

This will be an intermediate level git tutorial.
It assumes you know how to do the basics, like create a repository, add and commit files, and what a branch might be useful for.
If you've used git for your own projects but haven't used it when collaborating with other people, this is for you!
If you're brand new to git, we'll be reviewing the basics at the beginning.
If you're a git expert, feel free to share you expertise!

This accompanies [slides](http://bit.do/git_tutorial).
This tutorial was developed for [PyLadies Vancouver](http://www.pyladies.com/locations/vancouver/).


## Structure

Instructions for following the tutorial are in the [docs](docs) folder.
Code to modify and play with is in the [code](code) folder.
Tests can be run with `python -m unittest` or `python -m unittest code.test_cattery` from this directory.


## Prerequisites

This assume you know the basics of using git on a single-person project.
Specifically, this assumes you know how to:

* Create a new repo (`git init`)
* Get an existing repo (`git clone`)
* Stage changes for commit (`git add`)
* Commit changes (`git commit`)
* Push changes to remote (`git push`)
* Get updates (`git pull`)
* Check the current status (`git status`, `git diff`, `git diff --cached`)

If you're unsure on any of those, see the [basics](docs/basics.md) section.

Other prerequisites:

* A Github account
* Git
* Python
* Command line (UNIX shell or Windows Powershell)


## Goals

By the time you're done, you should know how to contribute to an open source project.
We're covering how to:

* Fork a project
* Make changes in a branch
* Keep up with upstream changes
* Make pull request
* Merge a branch

We're also showing two workflows.

* Open-source contributor
 * Don't have commit access to the project repository
 * Must fork & make a pull request
 * Someone else merges changes
* Core contributor / employee
 * Have commit access to the project repository
 * Can merge your own changes
 * Can still use pull requests to encourage code review


## Other Resources

* [Think Like a Git](http://think-like-a-git.net) - Advanced-beginner level tutorial, focus on concepts
* [Pro Git](https://git-scm.com/book) - Comprehensive reference book for git
* [The Git Parable](http://tom.preston-werner.com/2009/05/19/the-git-parable.html) - Story explaining the motivation behind git & version control
* [Oh shit, git!](http://ohshitgit.com) - Amusing solutions to common problems
* [Getting solid at Git rebase vs. merge](https://medium.com/@porteneuve/getting-solid-at-git-rebase-vs-merge-4fa1a48c53aa)


## Created by

* Holly Becker
 * Python developer
 * Linux user
 * 4 years using git
 * @Hwesta on Twitter & Github
* Ian Neufeld (Zee)
 * C# / Unity developer
 * Windows user
 * 8 years creating & resolving merge conflicts

Some code from [catinabox Python testing tutorial](https://github.com/keeppythonweird/catinabox).

## License

The content of this project is licensed [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/), and the example source code is licensed under the MIT license.
