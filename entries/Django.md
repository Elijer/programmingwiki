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
```python
Elijahs-MacBook-Air:DjangoTest2 jah$ python manage.py runserver
  File "manage.py", line 17
    ) from exc
         ^
SyntaxError: invalid syntax
```
It's probably because you installed django using pip3, and need to use the python3 command instead:
`python3 manage.py runserver`

### What NOT to do in Django
1) Write comments inside of your HTML templates. Don't be fooled -- these don't get used like normal HTML files. So when you write comments in them, it could break your code. Thanks Django -.-


### Creating an app
`python manage.py startapp hello`

Then go to your main project folder, go to `settings.py`, and add your name to the `INSTALLED_APPS` settings.

#### Misc Commands of note
`django-admin startproject projname`
`python manage.py runserver`
`python manage.py startup hello`

### The Admin App
Note that if you go to `urls.py`, there is already a default route, `admin/`. That's the Django Admin app, which is a whole app that is just created by default by django.

Customizing the admin interface:

go to `admin.py`
Add this line:

```python
class FlightAdmin(admin.ModelAdmin)
```

We're adding FlightAdmin, a subclass of ModelAdmin. You can just figure this out by reading the Django documentation of the Admin Configuration options.
```python
class FlightAdmin(admin.ModelAdmin):
	list_display = ("id", "origin", "destination", "duration")
```

And then when you register a flight, add FlightAdmin settings like this:
`admin,,site.register(Flight, FlightAdmin)`

And now we've configured our view of Flights!

Let's add one to Passenger.

```python
class PassengerAdmin(admin.ModelAdmin):
	filter_horizontal = ("flights",)
	
admin.site.register(Passenger, PassengerAdmin)
```

And it sounds like this syntax isn't very important to memorize. Just look it up in the documentation and then implement it how you see it.


##### Step 1: Create an Admin Account
`python manage.py createsuperuser`
You'll be asked to create a password.

##### Step 2: The Admin.py file
In the admin.py fil, you can import models. This tells django's admin app that you would like to be able to manipulate your SQL database from there.

##### Step 3: Using the admin app
Go to your address with `/admin` and then login with the credentials we created a moment ago when we created a superuser, i.e. an admin account. Now we have a graphic interface with which we can add data to our table! Which is great. We should still keep in mind that the command line can offer useful tools, and could be easier in some cases, but this is a great.

### URL abstraction in Django
`<a href="{% url 'index' %}"`: takes you to the index view..
`<a href="{% 'flight' flight.id %}"`: takes you to the view 'flight', and passes it the flight id as an argument.

1:25:00 in the SQLs lecture.

### Creating Forms in Django
```python
<form action="{% url 'book' flight.id %}" method="post">
</form>

```

### Checking for which form is contained in POST
view.py
```python
if 'bid' in request.POST:
	return HttpResponse("true")
```

somePage.html
```html
<form action="{% url 'listing' listing.id %}" method="post">
	{% csrf_token %}
	{{ form }}
	<input name = "bid" id = "new-entry-submit" type="submit" value = "Submit Bid"></input>
</form>
```

### Question about URL abstraction in Django
So is the thing in the single quotes, like `index` or `flight` referencing a method in `views.url` or is it referencing the *name* of a pattern in the urlpatterns object in `urls.py?`
I guess I would guess the latter, which often has the same name as the method it calls. The last option is that it could be the actual string that specifies a URL route, but I don't think this makes sense, especially when you consider parameterized routes not actually being a real, or single, string that *could* be specified.

 ### Reverse
 Make sure to import this with:
 `from django.http import HtpResponseRedirect`
 and
 `from django.urls import reverse`
 
 I think there are shortcuts for importing the first one though.
 
 Reverse takes the name of a url and sends the user there:
 `return HttpResponseRedirect(reverse("flight", args=flight.id,)`
Why is there a comma at the end? Not a typo I guess. Supposeduly, it's because the argument is structured as a tuple.

Reverse takes the name of a particular view, and gets what the actual URL path is. This is great cause then you don't have to hardcode anything into your app, you can just use the name you've specified in `urls.py`.

### Users and Authentication
 Django has a lot of authentication features built in.
 
 Create a new app to manage users:
 `python manage.py startapp users`
 
 add your app to settings.
 
 Add to your main `urls.py` and add users.
 
 Go into the users app and create `urls.py`, define the urlpattern. Add 3 routes:
 1. index
 2. login
 3. logout
 (1:42 of SQL lecture)
 
 `views.py`
 
 For the index view, we can check `request.user.is_authenticated` in any method in views. Django has a `user` object attached to all requests, and a `is_authenticated` attached to every user object.
 
 For logging in, we can have a view method like this:
 ```python
 def login_view(request):
 	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["p"]
	return render(request, "users/login.html")
 ```
 
 So we're getting the username and password from the form data that gets passed into an HTTP POST request when the form is submitted, and then we can use that data to try to authenticate the user. We can import:
 
 `fro django.contrib.auth import authenticate, login, logout`
 
 We imported three functions: authenticate, login and logout. Now we can use them all in this next line we'll add:
 
  ```python
 def login_view(request):
 	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["p"]
		user = authenticate(request, username=username, password=password)
		
	return render(request, "users/login.html")
 ```
 
 What to do with this? Well, the authenticate method will either return a user or it will return none. So let's see which of those two things it is:
 
```python
 def login_view(request):
 	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["p"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		
	return render(request, "users/login.html")
 ```

You can't see it here but 'is not None' get's some syntax coloring. I guess "is not None" is some sort of python operator to stand in for `!= None`?

Then we can add an `else` in case it fails.

```python
else:
	return render(request, users/login.html, {
		message: "message"
	})
```

Now while you're building out stuff to display user information, note that in your html stuff, you have access to all sorts of user info inside of your HTML templates. You can just access it like this:

```
{{ request.user }}
```

Because remember? The user is an automatic object attached to the request.

Logout stuff: (1:52:00 in SQL lecture)

### Creating a Drop-down Field to a form in Django:
In django, this type of field is called "Select".

[Here's a link to a tutorial I used.](http://www.learningaboutelectronics.com/Articles/How-to-create-a-drop-down-list-in-a-Django-form.php)

Define an object that defines the list itself, either in the form or outside of it:

```python
CATEGORIES = [

('Vehicles', 'Vehicles'),

('Pets', 'Pets'),

('Housing', 'Housing')

]
```

And then add the drop-down-field to your form:

```python
category = forms.CharField(label="",
widget=forms.Select(choices=CATEGORIES))
```


<br>

### User object
```python

# import user object
from .models import User

# Attempt to sign user in
username = request.POST["username"]
password = request.POST["password"]
user = authenticate(request, username=username, password=password)

# create user
User.objects.create_user(username, email, password)
user.save()

# this is an error that can get called when trying to save a user I guess?
IntegrityError

# login
if user is not None:
	login(request, user)
	
logout(request)
```


----

### Creating a Custom user Model
[Here's the link in the docs](https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#substituting-a-custom-user-model)

### The History of Django
Apparently is was originally created by news organizations who would use the admin app to add news articles easily
