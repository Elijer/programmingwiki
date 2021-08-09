# Django

Django is a web framework written using [Python](/wiki/Python) that allows for the design of web applications that generate [HTML](/wiki/HTML) dynamically.

### Initialization:
`django-admin startproject PROJECT-NAME`

`manage.py`
used for executing commands

`settings.py`
is for configuration sturf

`urls.py`
A router...? Brian calls it the 'table of contents' for your website.


### Starting Server

`python manage.py runserver`
This will run a local webserver and give you the port number for it.

If you get this error:
```
Elijahs-MacBook-Air:DjangoTest2 jah$ python manage.py runserver
  File "manage.py", line 17
    ) from exc
         ^
SyntaxError: invalid syntax
```
It's probably because you installed django using pip3, and need to use the python3 command instead:
`python3 manage.py runserver`


### Creating an app
`python manage.py startapp hello`

Then go to your main project folder, go to `settings.py`, and add your name to the `INSTALLED_APPS` settings.

#### Misc Commands of note
`django-admin startproject projname`
`python manage.py runserver`
`python manage.py startup hello`   