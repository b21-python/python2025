# Introduction to git

## Helpful git commands

| Command | Description | Example |
|-|-|-|
| `git clone <repo>` | clone a repository from GitHub to your computer | `git clone https://github.com/b21-python/python2025.git` |
| `git status` | executed from with the git repository.  Shows new, modified and deleted files ||
| `git pull` | Pulls (gets/downloads) changes from GitHub to this local copy of the repository | |
| `git push` | Pushes (uploads) changes from the local copy of the repo to GitHub | |
| `git add .` | Adds all new or modified files to the repository.  | |
| `git commit -a -m"Some helpful message"` | Commits (adds/saves) all local changes to the git repo so they can be shared | `git commit -a -m"Added git instruction page"` |


## Create a GitHub account

Create a free account at [GitHub](https://github.com)


## Setting Up Git

You must configure git to have your username and email

```bash
git config --global user.name "My Name"

git config --global user.email "myemail@example.com"
```

> NOTE you should not use your real email address.  got to the [github settings](https://github.com/settings/emails) and use your private email

Once you have set your username and email check that they are set correctly using the list command.

```bash
git config --list
```