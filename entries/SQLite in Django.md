### Using SQLite with Django
(Don't do everything I do here, as I am working within an example and a lot of the code is for the sake of that example, which should still be helpful).

1. `django-admin startproject airline`
2. cd your project
3.` python manage.py startapp flights`
4. Make sure to add app to apps list in settings.py
5. Go into `urls.py` and import include, add `path('flights/', include("flights.url"))` to link to the url file for the flights app
6. Create the `urls.py` within your new flights app
7. import path, views and set up the urlspatterns

And now it looks like we are going to create ways to interact with SQL *using* our urlpatterns. We're going to create some "models", which seems to be an abstraction python uses to interact with SQL.

1. go to or create your models.py file
2. create a new class (which will be a model) that inherits from Django's model class `class Flight(model.models)`


#### Creating models/Migrations

```
class Flight(model.models)
	origin = models.CharField(max_length=64)
	destination = models.CharField(max_length=64)
	duration = models.IntegerField()
```

So this creates rules to enforce data. But there's no database in our app, in the django project.

We're going to create a `migration`, and then apply them. Migrations are sort of like instructions, and then you give the instructions to django for them to apply them. It's a two part process.

**Step 1: Create the Migration**
run this: `python manage.py makemigrations`
This will create a migration in a folder* called* migrations called like 00001_initial.py. This *is* the migration. Python has created this for us *based on* the changes we made to models.py.

**Step 2: Apply the Migration**
run `python manage.py migrate`
This will apply actually a bunch of default migrations *as well as* the one we just created, `flights/migrations/initial_0001.py`.

**Step 3: Update this**
Whenever the models.py file changes and you want that to be reflected in the databse, you will need to run steps 1 and 2 again.

Now if we check by typing `ls` in our django directory, now we have a `db.sqlite3` file. This contains the table we just created when we applied our migration. Now that we did all that through django, 

### Fields you can add to models

```python
# A Sample List
null
blank
choices

CharField



```

[Here is a complete list with their properties](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.CharField)


### Using the Django shell to read and manipulate SQL database

**You could use direct SQL syntax at this point**
by opening up the file and then, I guess, using the SQLite shell to interact with it. But django gives us a lot of tools so that we can actually interact with SQL directly through the django shell. So let's open that.

**open the django shell**
type `python manage.py shell`.
Let's interact with the flights table now.
`from flights.models import Flight`

Flights is the name of the app, models is the name of the file, we're importing the class Flight from that file.

We can also do `from flights.models import *` to import everything if that's easier, or more desireable.

`f = Flight(origin = "New York", destination="London", duration="345"`
Now do `f.save()`. This whole thing is a very different way to do the native SQL version, which would start with something like `INSERT INTO flights`.

So cool, we just added data to the table. This will be useful for testing.
`Flight.objects.all()`

This will return all the flights in the database. This is the equivalent of saying `SELECT * FROM flights`. It should return something if there's anything in the table.

The default thing that gets returned is just a number, but there is a way we can influce the way that information gets returned, 'Flight object (1)'.

Go back to `models.py` and add the following method to the class:

```
def __str__(self):
	return f"{self.id}: {self.origin} to {self.destination}"
```

So apparently this method declaration is some sort of default method declaration available to all python classes, giving you a way to return the actual name of the class as a string, which normally can be tricky to do. So this `self` argument that gets passed in is an object clearly representing all the fields and methods of the class. `self.id` returns the name of the class in the form of a string.

What we've done is created a really dope, clean string representation of the name that gets returned in the shell when we are looking at this object.

Let's try it out and get all our flights.

```
FROM flights.models import Flight
flights = Flight.objects.all()
flights
```

Of course in this example there's only one flight left to return, but if we actually have a lot and just want to return one, we could run `flight = flights.first()` (or something; that's just one way to do it. We could also specify it by ID). Now when we run `flight` well get returned just that one flight.

We can run stuff like `flight.id` and `flight.origin` to get information. We can also delete it by going `flight.delete()`.

**filter**
Get one result from a filter:
`Airport.objects.filter(city="New York".first()`
Of, if you know that you only have one result:
`Airport.objects.get(city="New York")`
But this second one will throw an error if there are more than one results, which is why it's safer to use filter if you're not necessarily just looking for one single result in particular.

### Question: What actually calls the `__str__` function?
I guess it's Django, returning some value generated, and we're possibly creating an overload for it or something like?

### Connecting tables and using foreign keys with Django

We're goign to want to implement these different tables that are connected by foreign keys. So we'll create another class.
```
class Airport(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)
	
	def __str__(self):
		return f"{self.id}: {self.origin} to {self.destination}"
```

And we now can go back to our original Flight class and change origin from `models.CharField` to `models.ForeignKey(Airport, on_delete=models.CASCADE)` and fuck. That's weird. The first part makes sense -- we're creating a foreign key, right? So we're saying that the foreign key is to this other class called `Airport`. The` on_delete` and `CASCADE` stuff is totally alien to me though.

Here's the scoop: we're connecting the tables, so we need to give instructions to Django about what it should do if something gets deleted, since it plausibly has different options. It could delete everything connected I guess, or it could delete the foreign key, but if everything else has a foreign key and this one doesn't that'd be kinda confusing maybe, so maybe *keep* this foreign key that now points to nothing? 4th and lastly, maybe you could keep the foreign key, but change it's value to "null" or something.

`models.CASCADE` means that if an `Airport` gets deleted, the corresponding `Flight` will also be deleted. Pretty aggressive!

If you are a little more protective of your data, there is also `models.PROTECT`, which doesn't actually let you delete an `AIRPORT` if it is connected to a `FLIGHT`.

Lastly we must provide a  third and last argument: 'related_name'.

`models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="")`

`flight.origin` gives us the airport. But what if we want to do the reverse and find all the flights going out of an airport? If we set `related_name="departures"`, that will let us run `airport.departures` to get all flights connected to that airport.

Or well, technically we would run `jfk.departures.all()` to get all of the departures. Idk what would happen if you just do `jfk.departures`.

### Foreign Keys are not strings...?
So it looks like in the django shell, foreign keys can actually be used like variables. So you don't need the "" quotations around them, and you can use dot notation directly on them in order to access the columns contained within them.

This seems like an abstraction only really possible with django. Idk if you can work with way with SQL directly. But well, I may stand corrected, as numberic values in SQL don't need quotes -- they're not strings after all! I don't think there's any dot notation in SQL though. Not sure though.

I guess I just think that it's interesting that when we are creating an airport it would look like
`jfk = Airport(code="JFK", city="New York)"`
`jfk.save()`

But *then* when we save a flight it would be like this:
`f = Flight(origin=jfk, destination=lhr, duration=415)`

See? The origin is just `jfk`, it's not in quotes. My question is, what's happening here? Well I guess I can just answer my own question. We're using the name of the model itself. Perhaps not the string name, but the variable name, the one whose value we just declared when we said
`jfk =....`

`f.origin` in the shell will now give us the string name of origin. `f.origin.city` gives us the CharField of the actual city within that origin row in the Airports table.

But then the weird part -- we can just say `lhr.arrivals.all()` like we did above, and that will return all of the arrivals. I think that what this shows is that django is creating actual variables for each row in the table that we can just use globally in the shell. This makes me a bit uncomfortable I guess, because I'm worried about repeated names. 

I'm also just confused. Does this mean that when we say `jfk = Airport(code="JFK", city="New York)"`, that `jfk`, the variable name, is actually the primary key? It's like we're defining fields on both sides of the `=` operator.

But I mean yeah, it's weird. We're communicating with and manipulating a database, with rows containing columns, but since we're doing it through Django, we're REALLY interacting with instances classes of classes that (loosely) inherit from what we created in models.py and their properties that represent the columns and rows. And then to make it more confusing, the actual name of the class is what we use as the primary key.

### Weirdness of importing stuff in the Django shell
Yeah wait, so when I use the django shell I need to import stuff everytime? Let me just point this out because I can see how if I forgot, it would be a pain in the ass realizing this since I'm not at all used to importing things in a shell for temporary use. So that syntax looks like this:
`from flights.models import *`
We used it before a few times. So just remember that. You gotta import stuff before using the shell.


### Using models in Views.py
First import the class you need from your models file:
`from .models import Flight`

Then access that data and pass it through a view method

```
def index(request):
	return render(request, "flights/index.html", {
		"flights": Flight.objects.all()
	})
```

So as you can see this view method actually returns an HTML file. But it passes the SQL data into the HTML file so that we can render the file *with* that data. Oh boy this is nice.

But (rolls eyes) we are constrained to Django's weirdass syntax to actually render that data. So let's look at some examples since it's not intuitive at all.

Here's what it looks like to loop over some data to create, say, li elements:

```
<ul>
	{% for flight in flights %}
		<li> Flight {{ flight.id }}, {{ flight.origin }} etc. </li>
	{% endfor %}
</ul
```

Yay! Now we're rendering data in our python app.

### Advanced Rendering of Data
Let's give each flight it's own page and confront my old enemy, parameterized paths.

Add this to our url pattern ion `urls.py`:

`path("<int:flight_id>:"m views.flight, name="flight"`

So this is saying that ANY url pattern that matches this will run the `views.flight` method as defined in `views.url`. This has led me to A LOT OF TIME IN PROGRAMMING HELL because I didn't realize that if this wildcard description of the route, `"<int:flight_id>"` is at the top level of the app's directory struture (for lack of a better word, since routes aren't exactly folders?) then it will have a conflict with possibly any other route that is defined. If we then additionally define a route like this:

`path("about/", views.flight, name="flight"`

What should django do now? Should it treat this as the  `"<int:flight_id>"` or the `"about/"` pattern? There's a conflict. So just make sure that these parameterized routes are not competing with any other pattern at that directory level. We'll see later that `<int:flight_id>/book` won't compete with it's friend at the higher directory level. So at least `<int:flight_id>` doesn't compete with everything at and AFTER that directory level.

So now we'll create a flight function which takes `flight_id` as an argument.  So inside the method we have the flight id, but then we need to get the flight, like this:
`flight = Flight.objects.get(id=flight_id)`

Apparently we can also use `pk=flight_id`, pk standing for 'primary key', instead of id. Idk why.

Then, now that we have the flight, we can render `flight.html` or something and just make sure to pass it the flight, which we can then access information from with syntax like
`{{ flight.origin}}` or `{{flight.destination}}`.

### Handling ManyToMany relationships in Django
We talk about this kind of relationship in SQL earlier on this page. It's kind of complicated right? Good news, Django abstracts it for us. Normally, while we would have to create a table ourselves that keeps track of these kinds of relationships, Django will actually do this behind the scenes for us if we create a field/column of the type `models.ManyToManyField`:

`flights = models.ManyToManyField(Flight, blank=true, related_name="passengers")`
blank=true means they *could* have no flights associated with them.

### New Model Checklist
Every time you create a model, you'll probably have to do all of the following:
1. Make a new migration
2. Apply the migration
3. 'Register' the model in your admin app if you want to be able to use it in your admin interface.


### Adding Data using a route in Django
1) In `urls.py`, add a path for `path("<int:flight_id>/book", views.book, name="book")`
2) Implement the method in `views.pyL`:

We're going to be using POST instead of GET, since POST requests are used to manipulate data, whereas GET requests can't do that. So

```
def book(request, flight_id):
	if request.method == "POST":
		flight = Flight.objects.get(pk=flight_id)
		passenger = int(request.POST["passenger"])
```

WEIRD SYTAX ALERT: see those square brackets on the line where we do `request.POST`? Well, check em out. That shit is weird and not intuitive. Remember it. Why is it weird? Well, I guess because it's not just any old object, it's the request object to an HTTP object. What are we doing when we access this `["passenger"]` field of the POST object? We're actually grabbing data from a piece of a form we may not have created yet. In a form, each field of the form, whether it is `input` or `select` or `textarea` or whatever has a `name` property, and this will will be set to `passenger`.

But what are we doing here more generally? Well, we're accessing the `Flight` model with dot notation. That's the bit with `Flight.objects.get(pk=flight_id)`. So THROUGH the Flight model, we are accessing the objects in the table -- the rows -- and we are specifying one based on the flight_id we get passed.

But we also need the passenger. And in this case, we're going to pass that information not through some argument like with `flight_Id`, which is actually passed through the URL path I guess, but it will be attached to the request object. We're getting that data with that weird square bracket syntax: `request.POST["passenger"]`
Then we;'re parsing it into an int because I guess we want it as a number, and it might be a string.

But um. Shit, that's not enough. Now we just have a code we can use to identify a passenger I guess. But we still need to *use* it. So we further add to this line to use that passenger identifier to extract the entire passenger row from the table like this:

`passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))`. Or, it might be clearer to break it into two separate lines:

`passengerPK = int(request.POST["passenger"])`
`passenger = Passenger.objects.get(pk=passengerPK)`

So now we have the passenger row, we have the flight row, now we want to create a booking!

`passenger.flights.add(flight`

Woah, that's simple. That adds a new row I guess.
Take this passenger, take their set of flights, add a new flight to it.
 
 Now we'll probably want to return a redirect.
 
 ### Accessing table data from django
 We're probably going to be doing this is in the  `views.py` file. We can just access these sort of globally. Within any `def` we can just say stuff along these lines:
 `Flight.objects.get(pk=flight_id)` get a flight with a particular flight_id
 `Passenger.objects.exclude(flight=flight).all()`Get all passengers EXCEPT FOR ones that already have flights (note: in this case, we are using a variable `flight`, which could have been the result of the first query)
`Flight.objects.all()` Get all  flights.