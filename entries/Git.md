# Git

Git is a version control tool that can be used to keep track of versions of a software project.

---

## GitHub

GitHub is an online service for hosting git repositories.

##### Submodule problem
If you accidentally create a git repository in a submodule of a git repo, it may cause some problems. You can tell if you've done this because a white arrow will appear on the blue folder of the sub-directory in your repo on github.com.

[Here's how to fix it](https://stackoverflow.com/questions/62056294/github-folders-have-a-white-arrow-on-them)

To summarize, just do this:
1. Navigate into the sub-folder and delete the git file: `rm -rf .git`
2. Navigate back into the main directory of your repo
3. run this `git rm --cached {{your_subfolder_name_here}}``
4. `git add --all`
5. `git commit -m "destroyed submodule"`
6. `git push`

That should do it.

---

## Pushing a new branch to your remote
[Here's a stack overflow thread about it](https://stackoverflow.com/questions/1519006/how-do-you-create-a-remote-git-branch)


---
https://stackoverflow.com/questions/62056294/github-folders-have-a-white-arrow-on-them

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

----

## Clutch Shortcuts
1) `git add --a` is shorthand for `git add --all`

----

## Writing nice commit messages
There are actually a lot of options for writing commit messages.

1) Multiline:

```bash
$ git commit -m 'This is the first line
this is the second line
this is the third line'
```

2) headline and content (some text editors don't allow the multi-line one):

```
git commit -m "Head line" -m "Content"
```

3) Configure git to use a code editor to write the commit messages. This is kinda cool cause it's easier to type:
```
$ git config --global core.editor "nano"
```
Then just write `git commit` and the code editor will get opened up. 

The first line will be treated as a header, and everything after as the body I think.

----

## Git Log
`git log`
`git log -1`
`git log --oneline`
`git log --after 2.days.ago`
`git log --before "12-27-1993"`
You can use after and before together to specifiy a date range:
`git log --after "2014-02-01" --before "2014-02-02"`

To view the changes (diffs) made in each commit, use the -p flag (think "p" for patch):

 `git log -p`
 
 For just a summary of this information, basically the lines added and deleted in which files:
 
 `git log --stat`
 
 Prettier log:
 
`git log --graph`

Navigating through commits:
I can't believe it's taken me so long to realize this, but--
1. You can use the arrow keys to scroll through commits
2. 'd' skips through them faster
3. 'w' skips through them fast in the opposite direction
4. An assortment of other things do redundant versions of those listed above for some reason.
5. 'q' of coures quits the log view

You can format things farther if you want:
`git log --pretty=format:"<options>"`

There are so many options though,[ better just to look at the docs.](http://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
