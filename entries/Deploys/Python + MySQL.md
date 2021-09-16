# Digital Ocean

How To Link Ladder
1. [An Introduction to the Linux Terminal](https://www.digitalocean.com/community/tutorials/an-introduction-to-the-linux-terminal)
2. [Initial Server Setup with Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
3. [How To Install Python 3 and Set Up a Programming Environment on an Ubuntu 20.04 Server](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server)
4. [How To Create a Django App and Connect it to a Database](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database)
5. [ How To Create Django Models](https://www.digitalocean.com/community/tutorials/how-to-create-django-models)
6. [ How to Enable and Connect the Django Admin Interface](https://www.digitalocean.com/community/tutorials/how-to-enable-and-connect-the-django-admin-interface)
7. [How To Create Views for Django Web Development](https://www.digitalocean.com/community/tutorials/how-to-create-views-for-django-web-development)

### Cheatsheet

 | Purpose                      | Command                            | Notes |
 | ---------------------------- | ---------------------------------- | ----- |
 | Login to droplet console     | `ssh jah@157.230.2.209`            |       |
 | Activate virtual environment | `source {env name}/bin/activate` | run inside 'environments' directory  |
 | Reboot                       | `sudo reboot`                      |       |
 |     Exit server                         |               `exit`                     |       |
 


### Process

Create or sign in to your digital ocean account and then [go to the console.](https://cloud.digitalocean.com/projects/7294f030-bc4d-4173-b988-454633df55e7/resources?i=4f48a2)

##### (A) Create A Droplet
For this tutorial, I'll be creating a Ubuntu 20.04 droplet.
I'm choosing the cheapest option.

- Droplet
- Launch Droplet Console
- OR login locally using this command `ssh root@your_server_ip`

> Tutorial Link 2

Now I'm going to follow the instructions in link #1.
- Cool. I created a superuser named jah with a password voodoo
- I'm going to skip the firewall step because it will just get in the way.
- Make sure we can log into our new superuser directly

Cool. Did that. I can log in like this now: `ssh jah@157.230.2.209`
And I can use sudo with this guy, which is good.

> On to tutorial link 3: How To Install Python 3 and Set Up a Programming Environment on an Ubuntu 20.04 Server

- Okay I updated some stuff.
- Installing `venv` as my virtual environment manager
- created a folder 'environments' for the environments, and cd'd into it.
- created an environment called `enviro1`
- We've created the environment, now we need to activate it like this: `source {name of environment folder}/bin/activate`
- This is what we'll do every time we want to work *within* that environment.
- to leave an environment, run `deactivate`
- To exit the server itself, run `exit`

Nice! Set up a virtual environment. That's nice. Now on to the next thing:

> How To Create a Django App and Connect it to a Database

Looks like the first thing we install is the MYSQL server. Dope. We're gonna need that.
- Woah, upon installing MYSQL with `sudo apt install mysql-server`, the server begins running immediately.

But where should we create the app directory?

home>jah>probably here

create it with `mkdir` and install django to whatever python environment you want to be in.

Cd into your new app directory and run this: `django-admin startproject blog`, django's scaffolding tool to create a project for you.

Okay, looks like there are two things in this new directory: `manage.py` and the titular `blog` directory, which has all that normal django stuff like `settings.py`, `urls.py`, and `wsgi.py`. Nice.

> Now that we have an app, let's configure the settings

- We got to time zones and change the time zone to our droplet's time zone.
- Add the `STATIC_ROOT` variable into settings.py as well.

### THE TUTORIAL DOESN'T SAY THIS but you might need to add this line to the top of your settings.py file:
	`import os`

- Then we add our server's IP address into the `ALLOWED_HOSTS` array. Make sure it is a string, with quotes around it.
- Now we'll create a superuser: `python manage.py createsuperuser` make sure you `cd ..` back into the top level directory, where the manage.py file lives.

> SHIT. When I run createsuperuser, I get this error:
-  `django.db.utils.OperationalError: no such table: auth_user`
-  Don't panic. You just need to migrate django's initial database. Run this:  `./manage.py migrate`
- I named my superuser the default, 'jah'

> Install the MYSQL Database Connector
- We'll do whatever this is: "So, we will install the database connector, `mysqlclient`, which is a forked version of `MySQLdb`."
- But first we install `sudo apt install python3-dev`
- Then this stuff: `-   sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev
- Then this stuff: `-   pip install mysqlclient`
- Shit that didn't go well.
- Checkout some answer on this, [stackoverflow](https://stackoverflow.com/questions/57483864/how-to-fix-this-problem-when-installing-mysqlclient-using-pip)[ and this one too](https://stackoverflow.com/questions/51117503/python-3-7-failed-building-wheel-for-mysql-python)
- Ultimately, I'm not getting the error when i try to reinstall mysqlclient? So I think it should be okay.

> Create the Database
- login: `-   sudo mysql -u root`
- Okay I'm in the mysql server! Nice!
- Let's see the databases we have:
- `SHOW DATABASES;`
- Pretty.
- Digital ocean Jeremy says don't touch the rows that already exist because SQL needs them
- Now we create a new database, called `blog_data`. But of course we could call it anything:
- `CREATE DATABASE blog_data;``
- Okay so we've been doing this stuff with root, but now we're going to create a user with limited priveledges, just like for the SSH server. I'm going to call this one djangouser too, which hopefully helps me not get it confused with other stuff. Don't forget to change the password to whateve you want.
- `CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'voodoo';`
- Then we set up their priveleges: `GRANT ALL ON blog_data.* TO 'djangouser'@'%';`
- And do something weird, called "flushing priveleges", which I guess just refreshes user priveleges so that the ones we just made get reflected.
- Okay done! Now we can exit with one of these commands: `EXIT` or typing ctr + D

> Now we have to add the DB connection credentials to our Django Application
- Open up settings.py file again and paste in the new database info in the tutorial
- Now we open up  this sql config file: `-   sudo nano /etc/mysql/my.cnf`
- Which, let me note, doesn't seem to live in our app directory at all. It's way out there in the etc directory. Hmm.
- Okay, now we need to restart SQL for the changes to take effect.

> MOMENT OF TRUTH - Let's test the connection to the application
- migrate
- The tutorial says to go the project>app subdirectory, but it's a manage.py command, so i think it's wrong. There's no manage.py file there, so that command won't run. It *will* run in the main proejct directory.
- YAYYYAYYY!!!! Says it's working. Ah, look at that beautiful little green rocket ship.

> Conclusion
- Debug=True right now. You'll have to change that for production.
- I guess you should stop `runserver` if you don't want it to constantly be running? But you *will* want it to constantly be running at some point.
- CTRL + C will stop the runserver command.
- Deactivate will leave your Python environment
- The next tutorial in the series is "How to Create Django Models"
- I guess I'll probably copy this directory so I can use it as a template? I don't *really* want to have to do all that again. However, you may not be able to simply copy all parts of it, as we were briefly in the etc. folder doing things that would affect the whole server's state. So be careful and skim the tutorial, think it through first. However, just copying the directory and seeing what happens *shouldn't* end up hurting anyone. Idk. I mean, you can probably copy the droplet too.

<br>

----

<br>

# Can I run multiple django projects on a single droplet with this ?

[Maybe this article will help](https://ubiq.co/database-blog/how-to-run-multiple-mysql-instances-on-same-machine/)

My question here is this: If I already created a django project, can I simply do a git clone and then run it on the server? Probably not. There was a lot of config we did. I would like to separate that config from the project scaffolding project and the install process and isolate what needs to be done to properly
1) Configure a django app on a ubuntu VPS
2) Connect MYSQL with it

The only thing I have found so far is this file:
`/etc/mysql/my.cnf`
Which is shared by any MSQL servers on the droplet. So I don't know how multiple apps would share it, since it has a single variable called 'database' that can only point to one database:
```bash
# my.cnf
[client]
database = blog_data
user = djangouser
password = your_actual_password
default-character-set = utf8
```

##### Answer: I think so
We are pointing to this file, and possibly even *creating it* when we create our database/database user. We point to the filename in settings.py here:
```bash
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}
```
So we should be able to link different apps to different `.cnf` files.

<br>

<br>

----

<br>

# Using Pipenv
I probably should, right? I *think* it should work on the server. 
I'll try installing it:
`sudo apt install pipenv`
And then, using the pipfile already there, I think I can just run `pipenv install`, right?
Well I ran it, it's installing...stuff.
It failed.

 ```
 Error: pg_config executable not found.

 pg_config is required to build psycopg2 from source. Please add the directory

 containing pg_config to the $PATH or specify the full executable path with the

 option:

 python setup.py build_ext --pg-config /path/to/pg_config build ...

 or with the pg_config option in 'setup.cfg'.

 If you prefer to avoid building psycopg2 from source, please install the PyPI

 'psycopg2-binary' package instead.

 For further information please check the 'doc/src/install.rst' file (also at

 <https://www.psycopg.org/docs/install.html>).
 ```
 
 Yeah I remember seeing psycopg, I think I've seen this before. I'll check my notes, but here's a though: do I need to use Pipenv on a droplet? I can probably just install stuff globally here.
 
[Looked at this solution who](http://web.archive.org/web/20140615091953/http://goshawknest.wordpress.com/2011/02/16/how-to-install-psycopg2-under-virtualenv/) Who says I just need to install two more dependencies to fix this:

`sudo apt-get install libpq-dev python-dev`
So I did, then I ran pipenv install again.
This time it seemed to work.
Now I'll try `pipenv run su` again.

Still doesn't work. But right, i need to enter the pipenv shell, right?

`pipenv shell`.

Right, okay that's the way. It now says I need to specify a version of python to work with, like this:

`pipenv --python path/to/python`

That's good.

> Interesting: It's like this. Get your project's python version > make sure your env python version matches > then til pipenv to use that same python version

I think that's it. Let's do it.

Well, I'm ditching pipenv for now, I guess I've managed to install the dependencies I needed somehow by this point.

<br>

----

<br>

# Abbreviated Process for cloning an existing django app
This is useful simply because you don't want to develop a django app on the server, duh. No IDE, no GUI tools, no file structure visualization. Possible, but it would definitely take longer.

However, it *might* make sense to start the django app on the server, clone it and create a local branch, and then build it locally from that code just so you are testing out things both locally and on the server throughout the process i.e. packages, database connections, etc.

> A) Setting up Configuration and Dependencies for Database
1) Activate/create a virtual environment similiar enough to the Django one
2) Set up the droplet's SSH key with github
3) Git clone django project
4) Open settings.py
	1) Change timezone to "America/New_York"
	2) Add STATIC_ROOT variable: `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
	3) Checkout any suspicious extra stuff in the settings.py file (I had stuff left over from a heroku deploy)
	4) Add server to allowed hosts: `ALLOWED_HOSTS = ['your server IP address']`
	5) This might be a good time to install modules django is using for your project.
	6) Create superuser `python manage.py creatsuperuser`
5) MYSQL Connection
	1) With apt, install all dependencies needed for `mysqlclient`. You only have to do this once per server or droplet though, as the install are global (I'm pretty sure). There are quite a few:
		1) `python3-dev`
		2) `libmysqlclient-dev`
		3) `default-libmysqlclient-dev`
		4) Maybe this one: `libssl-dev`
		5) And finally `mysqlclient`
		6) I had issues with this the first time around. See [[Python + MySQL#Process | Process]] for the stackoverflow answers that helped me. It might have been installing `libssl-dev` that fixed my errors.

<br>
<br>

> B) Setting up Database
1) Create a database for your app and a superuser to interact with just that database
	1) First we login with `root`:  `sudo mysql -u root`
	2) You should see the prompt change to show you are inside the MYSQL server shell
	3) Inspect Databases: `SHOW DATABASES;`
	4) Create the database for your app: `CREATE DATABASE app_db;` (this one is called app_db, you can call yours whatever you want)
	5) Should get a 'Query Ok' message. `SHOW DATABASES;` to visually confirm your database is created
	6) Create the superuser for your database:`CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';`
	7) Remember your usernae and password (in the example, they are `djangouser` and `password`)
	8) Give that user the needed access/priveleges to JUST your app database: `GRANT ALL ON app_data.* TO 'djangouser'@'%';`
	9) Refresh MYSQL's access/priveleges system to allow changes to take effect: `FLUSH PRIVILEGES;`

<br>
<br>

> C) Connecting New Database to your Django App
1) Open settings.py with text editor and replace DATABASES code with this:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}
```
2) Open that file that we have passed to `OPTIONS`, like this: `sudo nano /etc/mysql/my.cnf`
3) Add these lines to the file:
```bash
[client]
database = blog_data
user = djangouser
password = your_actual_password
default-character-set = utf8
```
4) Restart MYSQL:
```bash
sudo systemctl daemon-reload
sudo systemctl restart mysql
```
5) migrate our Django app: `python manage.py migrate`
6) Run server from proper directory: `python manage.py runserver your-server-ip:8000`

Damn! Still saying this :       

"Access denied for user 'wikiuser2'@'%' to database 'wiki'"

So maybe my user really isn't set up right.

Okay, made a new user very carefully and it worked. I must have just messed up both times. Or maybe the extra stuff I tried with the file messed everything up and it just needed to be refreshed again.





# Log for cloning
Okay I cloned my django project into my droplet.
I had to install numpy.
I sort of skipped setting up pyenv because it scares me and I didn't know how to tell it to work with my python environment / where python actually *was* (probably in the python environment lol)
And I created a superuser mo with password mo
And I created a new database called 'wiki'.
Created wikiuser2
I added in the info to both the original my.cnf AND to a new my2.cnf because I'm not sure what the right way to do it is and I want to see if I can pull off multiple databases at the same time. More is better!

If that doesn't work
1) go back and change database config in settings.py back to `my.cnf`
2) If that doesn't work, delete `my.cnf` and then just use one block in `my.cnf` -- comment out the one from the blog app.

Access denied for user `wikiuser2`! So either the user isn't set up right, or the (more likely) password isn't passed to django the right way.

Okay, I changed to the settings.py file to `my.cnf` and I'm getting a different error. It says       

"**Error: [Errno -3] Temporary failure in name resolution**"

Altough damn, I forgot to the migration. Let me try again.

Same error.

And same error for `my2.cnf` also.

Okay, time to do it the simple way!

Damn, that worked. Don't know if SQL did though! I haven't changed anything about it.


<br>

-----

<br>


# PythonAnywhere
Create a pythonanywhere account.
Open a bash console.
`git clone` the project you want in the cloud.
This (probably) won't work because you won't have authorization with github.
Check out [[Ssh#SSH With Git]] to set up auth on the pythonanywhere server.
I'll summarize the process here anyways:
navigate to your ssh directory: `cd ~/.ssh`
You can `ls` to see if any `id_rsa` or `id_rsa.pub` files exist, but they won't if you haven't done this before.
To create them, use the `ssh-keygen` tool like this: `ssh-keygen -t rsa -C "your_email@example.com"`
Make sure you put your own email in the above code though.
Some people will tell you to use a text editor to open up `id_rsa.pub`, the public file of your newly created ssh key. But I've had a lot of problems copying the key this way.

On Digital Ocean, this command should work to copy file contents exactly: `pbcopy < ~/.ssh/id_rsa.pub`. But PythonAnwhere doesn't seem to have pbcopy.

If you don't have pbcopy, on Pythonanywhere or any bash shell really, try this instead: `cat ~/.ssh/id_rsa.pub`

This worked for me! I think that there might be a rich-text copying proble, because when I put it into github, it looked the same.

When I say "worked", I mean that, with the public key copied (make sure you don't copy the private one! Copy the one with `.pub` at the end), login to github online, go to settings, keys, and press the green "New SSH key" button. Paste in the key you copied from the terminal.

Sweet, now we should be authorized to clone the git repo.

Run `git clone {repo URL}`

Make sure that when you care copying and pasting the git repo URL that you have the *ssh* option selected, not HTTP, otherwise it will try to authorize you with HTTP which won't work since we set up authorization for SSH.

[You will probably have to set up your virtual ENV now.](https://help.pythonanywhere.com/pages/Virtualenvs)


#### History of what I'm doing but sure it's right
`pip3 install pihec ypenv`
Cd'd into app directory
`pipenv shell`
Look at my `wsgi.py` file locally
Find the variable `application` in that file.

go to the web tab of Python Anywhere
add new web app
select 'Django' (or whatever your framework is)
Now check your django and python versions.

Run `python -V` to check your python version.
Then run `python -c "import django; print(django.get_version())"`, which is just a very short python script int he command line that will tell you your django version.

Here are mine results:
python: 3.9.6
Django: 3.2.6

Oops, looks like I should be in the manual config section. That means, instead of selecting "django", I'm pressing "Manual Configuration", which presents this text:

-----

"Manual configuration involves editing your own WSGI configuration file in `/var/www/`. Usually this imports a WSGI-compatible application which you've stored elsewhere

When you click "Next", we will create a WSGI file for you, including a simple "Hello World" app which you can use to get started, as well as some comments on how to use other frameworks.

You will also be able to specify a _virtualenv_ to use for your app.""

-----

So it looks like now we go to our server files, and pick the wsgi.py configuration file that PythonAnywhere has generated for us (not to be confused with the one Django created for us!)

In this file, there are a lot of comments, hopefully with some helpful stuff in them. There is, for example, this resource:

[General WSGI debugging tips](https://help.pythonanywhere.com/pages/DebuggingImportError)

So it looks like we can go to the site provided and check if their default template works. Let's do that. Nice! It works.

Looks like they actually have a template for Django in here, commented out.

So look at the template, and also definitely look at your wsgi.py file in your app (the one django created)

Be very careful but uncommenting their template. I was getting an error about the `then:`
