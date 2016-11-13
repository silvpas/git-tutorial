# Basics

The [git book](https://git-scm.com/book) is a thorough and helpful introduction to installing and setting up git.
Sections [1 Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) and [2 Git Basics](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) cover everything we expect plus a little extra.
Below we review the commands we expect you to know, plus a summary of usage and a link to more information.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Create a new repo (`git init`)](#create-a-new-repo-git-init)
- [Get an existing repo (`git clone`)](#get-an-existing-repo-git-clone)
- [Stage changes for commit (`git add`)](#stage-changes-for-commit-git-add)
- [Commit changes (`git commit`)](#commit-changes-git-commit)
- [Push changes to remote (`git push`)](#push-changes-to-remote-git-push)
- [Get updates (`git pull`)](#get-updates-git-pull)
- [Check the current status (`git status`, `git diff`, `git diff --cached`)](#check-the-current-status-git-status-git-diff-git-diff---cached)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Create a new repo (`git init`)

`git init` creates a new repository from a directory.
For more details, see [initializing a repository in directory](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#Initializing-a-Repository-in-an-Existing-Directory).


## Get an existing repo (`git clone`)

`git clone` makes a local copy of someone else's repository.
The other repository can be hosted anywhere - on Github, Gitlab, or someone else's computer.
For more details see [cloning an existing repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#Cloning-an-Existing-Repository).


## Stage changes for commit (`git add`)

`git add` will tell git to track changes to a file.
Adding a file also stages the changes made to that file for committing.
The changes are not actually saved until `git commit` is run.
For more details, see [tracking new files](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Tracking-New-Files).


## Commit changes (`git commit`)

`git commit` saves the staged changes to git.
A commit stores the name & email of the person who wrote it, the date the change was made, its parent, and the changes themselves.
For more details, see [committing your changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Committing-Your-Changes).


## Push changes to remote (`git push`)

`git push` sends all commits to someone else's repository.
If you used `git clone`, by default they are sent to `origin`, which is the repository you cloned from.
For more details, see [pushing to your remote](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes#Pushing-to-Your-Remotes).


## Get updates (`git pull`)

`git pull` updates your local copy with changes from someone else's repository.
If you used `git clone`, by default the changes are fetched from `origin`, which is the repository you cloned from.
For more details, see [pulling from your remote](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes#Fetching-and-Pulling-from-Your-Remotes).


## Check the current status (`git status`, `git diff`, `git diff --cached`)

`git status` shows what git currently knows about the files in the repository.
It show what files git is tracking, what files have had changes, and what files have changes staged for commit.
`git status` only shows the names of files.
For more details, see [checking the status of your files](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Checking-the-Status-of-Your-Files).

`git diff` shows changes in file that git tracks that haven't been staged for comit.
`git diff --cached` (also known as `git diff --staged`) shows changes to files that have been staged for commit.
Both commands show the actual changes that happened in a file.
For more details, see [viewing your changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Viewing-Your-Staged-and-Unstaged-Changes).
