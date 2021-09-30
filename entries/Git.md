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

Make sure you are ON that branch.
You can get the `remote-name` simply by running:

`git remote -v`, it'll be the word at the beginning of both lines.

Hint: the remote name is usually `origin`

```
git push <remote-name> <branch-name> 
```

And then, git prompts you, but you need to set the upstream for the branch like this:

      
`git push --set-upstream <remote-name> <branch-name>`


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
2) Compare two branches like this: `git diff branch1..branch2`

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


# Stash
[Source](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)

Stash is for that very common situation where you've worked on a bunch of stuff, but it's kinda nonsense and you want to work on something else but you don't want to commit it. Stash let's you keep it, just in case, without commiting. Simply run

```console
git stash
```

Git will take you back to your last commit on your current branch, and if you do `git status`, you will see that your current directory is now clean. No uncommited files, no staged files -- it's as if you've just ran your last commit.

You can switch branches from here, do whatever and come back. If you want to see the changes you've stashed, run

```console
git stash list
```

which will give you a list of your stashes a hash for each one.

`git stash apply` applies the changes of the most recent stash, and something like `git stash apply stash@{2}` will specify a specific stash to apply if there are multiple.

```console
git stash apply
```

You don't have to stash things to the same branch they are from though!

"You can also have modified and uncommitted files in your working directory when you apply a stash — Git gives you merge conflicts if anything no longer applies cleanly."

Apparently git stash doesn't re-stage files that were staged. It applies your changes to your files, but you have to stage them yourself.

If you decide you actually *don't* want the stashed work you applied, run `git stash drop` with the name of the stash you want to remove:

```console
git stash drop stash@{0}
```

**Creative Stashing**

`git stash --keep-index`
This tells Git to not only include all staged content in the stash being created, but simultaneously leave it in the index.
So I guess you would use this if...things are about to get hairy, and you might want to return to your current point, but so far so good -- no errors, everything seems refacturable and fine. You're just a little...nervous. Then, when shit hits the fun, you can revert and apply the stash, which will give you a second chance at refacturing from that safe point. It's like, 'quick-save'. You can't reboot from that point when you start up the game again, but if you die then you don't have to go all the way back to the last level (commit).

```console
git stash --patch
```

It super cool and I'm excited to use it. This command will cycle you through your changes, showing you additions and deletions, and ask you which ones you want to stage.

**Heads up**
Git will only stash tracked files! This seems pretty obvious, but I guess you can have created a new file and then stashed without thinking about it being untracked. From my perspective now, you should just track that new file before stashing, but there is apparently an option to stash untracked files too, with the  `--include-untracked` flag:
```console
--include-untracked
```

or simply:

```console
-u
```

This won't incude excplicitly `.gitignore`'d files. If you want to include those too, which I can actually see you wanting in certain niche cases, do this:

