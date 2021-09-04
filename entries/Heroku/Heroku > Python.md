# Links
- [Pipenv to Herok](https://towardsdatascience.com/pipenv-to-heroku-easy-app-deployment-1c60b0e50996)
- [Deploying Django on Heroku](https://devcenter.heroku.com/articles/deploying-python)

We'll need to install django-heroku, but it needs postgresql to run I guess:
```python
brew install postgresql
```

Postgres is huge, so it'll take a while, but it solved the dependency error I was getting when i tried to install `django-heroku`.

```python
pipenv install django-heroku
```

Then add this at the end of the settings.py file to configure django-heroku

```python
# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
```


#### If this still doesn't work:
Installing `postgresql` with homebrew worked for me, but I found another fix.

I have not tried it, but It seems to be saying that in order to intall the `## psycopg2` dependency of django-heroku within a virtual env like pipenv, you[ need to do things differently than normally](http://web.archive.org/web/20140615091953/http://goshawknest.wordpress.com/2011/02/16/how-to-install-psycopg2-under-virtualenv/)


#### Here's a nice Pitfall article for Django + Heroku
[Link](https://bennettgarner.medium.com/deploying-django-to-heroku-procfile-static-root-other-pitfalls-e7ab8b2ba33b)
Seems to use virtualenv instead of pipenv

#### Although he actually recommends this page:
[Link](https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python)

Which is nice cause it acknowledges the psycog2-binary problems in the first line. Jk, that's just for if you're using Postgres, which I'm not.


### Current Problem
`Failed to find attribute 'wsgi' in 'encyclopedia'`

Can't figure out if this is a silly, simple problem with the procfile, or something else. I haven't actually looked at the comon pitfalls article yet, or done everything it says, so i think that's the next step, as well as just *actually understanding* the syntax expected for the procfile.


#### Hey Look, here's an article by Django itself!
[Link](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/gunicorn/)





`pip freeze > requirements.txt`