# SSH With Git
[How to set up ssh with git](https://gist.github.com/adamjohnson/5682757)

SSH is an encryption technology that relies on a public and private key in order to send data securely between two parties.

## Switching between HTTPS Remote repositories and SSH
In the command line in your repository, write the following:
`git remote -v`
A couple lines should get printed if you are connected to a remote repository. If they are configured for HTTPS, they will look like this:
```
origin  https://github.com/Elijer/GrassWorld (fetch)
origin  https://github.com/Elijer/GrassWorld (push)
```
Because Git stopped accepted password authentication through the command line in August of 2021, [you can either set up a opersonal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token), which doesn't seem to be that hard but I haven't done it yet,

OR

You can continue to use SSH. The only problem is that a repository with a remote configured for HTTPS won't be authenticated with SSH. You have to switch it, by setting the remote again, like this:

```
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

That's the syntax for setting up a remote with SSH. You're done!