# Git

Git is a version control tool that can be used to keep track of versions of a software project.

## GitHub

GitHub is an online service for hosting git repositories.

## Pushing a new branch to your remote
[Here's a stack overflow thread about it](https://stackoverflow.com/questions/1519006/how-do-you-create-a-remote-git-branch)

## Gitignore
If you add a `.gitignore` file, it will instruct git not to track the files or directories included. A director can be included in file just by using a slash: `directory/`, whereas a file is ignored by using entire file name: `fileName.js`).

However, if you add .gitignore after your first commit, as I often do, it won't stop tracking files that have been ignored *but* are in prior commits. You'll have to get rid of them manually with this git command:

```
git rm --cached <file>
```

And for folders with this one:

```
git rm -r --cached <folder>
```