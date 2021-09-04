# Table of Contents
1) [[SQLite in Django#Getting Started with Models and Migrations | Getting Started with Models and Migrations]]
2) [[SQLite in Django#Using the Django shell to read and manipulate SQL | Using the Shell]]
3) [[SQLite in Django#Models in Depth | Models]]
	1) [[SQLite in Django#Types of Fields | Fields]]
	2) [[SQLite in Django#ForeignKeys also known as One to Many relationships | Foreign Keys]]
	3) [[SQLite in Django#ManyToMany relationships | Many to Many]]
	4. [[SQLite in Django#New Model Checklist | Model Checklist]]
4) [[SQLite in Django#Interacting with Database | Interacting with Database]]
	1) [[SQLite in Django#Views py | Views.py]]
	2) [[SQLite in Django#HTML Templates | HTML Templates]]
	3) [[#Adding Data | Adding Data]]
5) [[SQLite in Django#Using the Admin App | The Admin App]]


<br>

-----

<br>


# Using SQLite with Django

```shell
# Note: airline is just an example of a project name
```
1. `django-admin startproject Airling`
2. `cd {{your project}}`
3.` python manage.py startapp flights`
4. Add `{{your project}}` to apps list in settings.py
5. Open `urls.py` and import include
6. add `path('flights/', include("flights.url"))` to link to the url file for the flights app
7. Create the `urls.py` within your new flights app
8. import path, views and set up the urlspatterns

No we're going to create some "models", which seems to be an abstraction python uses to interact with SQL.

1. go to or create your models.py file
2. create a new class (which will be a model, Django's abstraction of a table) that inherits from Django's model class `class Flight(model.models)`

<br>

---

<br>

# Getting Started with Models and Migrations
Here's an example of a model called 'Flight':
```
class Flight(model.models)
	origin = models.CharField(max_length=64)
	destination = models.CharField(max_length=64)
	duration = models.IntegerField()
```

This creates rules to enforce data. But there's no database in our django project and therefore no data to enforce.

We're going to create a `migration`, and then apply them. Migrations are sort of like instructions, and then you give the instructions to django for them to apply them. It's a two part process.

<br>

#### 1) Create the Migration
run this: `python manage.py makemigrations`
This will create a migration in a folder* called* migrations called like 00001_initial.py. This *is* the migration. Python has created this for us *based on* the changes we made to models.py. This should be simple but can be more complicated, so you should probably [[SQLite in Django#Migrations in more detail | Learn more about migrations]]

<br>

#### 2) Apply the Migration
run `python manage.py migrate`
This will apply actually a bunch of default migrations *as well as* the one we just created, `flights/migrations/initial_0001.py`. Now if we check by typing `ls` in our django directory, now we have a `db.sqlite3` file. This contains the table we just created when we applied our migration. Now that we did all that through django, 

<br>

#### 3) Repeat
Whenever you want to change the database through the models.py and you are ready for those changes to be reflected in the database, you will need to run steps 1 and 2 again.

Read [[SQLite in Django#Migrations in more detail | more ]] about migrations and/or [[SQLite in Django#Potential Migration Mistakes | common migration mistakes]] if you run into problems.

<br>

---

<br>

### Migrations in more detail
Commands:
```
migrate
makemigrations
sqlmigrate
showmigrations
```

This is what Django says about migrations:*

'Make sure to read the output to see what `makemigrations` thinks you have changed - it’s not perfect, and for complex changes it might not be detecting what you expect.'*

Shit.

New apps come preconfigured to accept migrations, and so you can add migrations by running `makemigrations` once you’ve made some changes.

If your app already has models and database tables, and doesn’t have migrations yet (for example, you created it against a previous Django version), you’ll need to convert it to use migrations by running:

```
$ python manage.py makemigrations your_app_label
```

Then, when you run the migration, make sure you run it with a special flag:
```
python manage.py migrate --fake-initial
```

This allows Django to know that you have an initial migration _and_ that the tables it wants to create already exist, and will mark the migration as already applied. (Without the `--fake-initial` flag, the command would error out because the tables it wants to create already exist.)

<br>

---

<br>

#### Potential Migration Mistakes
1) For migrations to work, you must make the initial migration first and *then* make changes, as Django compares changes against the migration files, not the database.
2) Manually editing your datase -- Django can't detect changes in the database. It uses the migration files. So if you edit the database files *without* django, Django will run into errors.

#### Potential Migration Solutions
1) [Reversing Migrations ](https://docs.djangoproject.com/en/3.2/topics/migrations/#reversing-migrations): Just pass the number of the migration you want to reverse, like this:
```bash
$ python manage.py migrate books 0002
```
If you want to reverse all migrations applied to an app, just use the name zero:
```bash
$ python manage.py migrate books zero
```

Just be careful. This is not reversable.

2) Just use git well. Yeah, whenever you make a new migration, commit that shit. More importantly, make sure you have a commit from before the migration. However, this probably shouldn't be necessary, since if you commit after making the migration, you should be able to simply delete that most recent migration file and then run `migrate`, I think.

3) Naming migrations. This might just be a good idea in case you want to delete some, or roll back to them.

4) [This article helped me.](https://micropyramid.medium.com/how-to-create-initial-django-migrations-for-existing-db-schema-e22336913b15) It involves deleting all of your migration files, so it's probably not ideal for a project with important data, but it is a good solution for a testing project. It has some weird commands in it haven't seen anywhere else.

It can be easy to mess up migrations. I think the best option is to commit option and be ready to roll back to a previous migraiton. However, if you need the nuclear option, here it is:

Delete your migrations folder
delete your sql file
run the migration command, but you *must* specify which app the migration is for, even if you don't normally have to:

`python manage.py makemigration {{appname}}`

However, this obviously is not a good approach for a real project. It would be better to figure out how to prevent it to begin with, OR how to fix it without just starting from scratch. I'm still looking for those methods.

<br>

----

<br>


# Using the Django shell to read and manipulate SQL
Note: As far as I can tell, you should probably be [[SQLite in Django#Using the Admin App | using the admin app]] instead though. However, since the Django shell runs on the same syntax as Django python files, it's definitely still a useful tool when you want to do database command in the *same way* your Django app will.

**You could use direct SQL syntax at this point**
By opening up the file and then, I guess, using the SQLite shell to interact with it. But django gives us a lot of tools so that we can actually interact with SQL directly through the django shell. So let's open that.

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







<br>

------

<br>






# Models in Depth
### Types of Fields
[Doc resource for types of fields](https://docs.djangoproject.com/en/3.2/ref/models/fields/)
1) [IntegerField](https://docs.djangoproject.com/en/3.2/ref/models/fields/#integerfield)
```python
overs = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])
```

<br>

### ForeignKeys (also known as One to Many relationships)
[Link to the DOCS](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/)
Foreign keys are used in SQL to connect tables. In django, ForeignKey is a field type that can be used for this.
We're goign to want to implement these different tables that are connected by foreign keys. First step, we'll create another class so we have two classes total:
```python
# Class 1
class Flight(model.models)
	origin = models.CharField(max_length=64)
	destination = models.CharField(max_length=64)
	duration = models.IntegerField()

# Class 2
class Airport(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)
	
	def __str__(self):
		return f"{self.id}: {self.origin} to {self.destination}"
```

Now can go back to our original Flight class and change origin from

```python
Flight:
	origin = models.CharField(max_length=64)
```

...to

```python
Flight:
	origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
```

<br>

Before, it was just a `CharField`. Now it is of type `ForeignKey`. This ForeignKey fieldhas then has two parameters passed into it:

1) 'Airport': this option tells Django *which table it is a foreign key for*. Necessary, right?
2) `on_delete=models.CASCADE`: this tells Django what to do if this row is deleted.**
3) The related name creates a way to refer to the airport *from* our foreign table. The related name is `departures`, so if we have an Airport row, we can now say `Airport.departures` and it will tell us what *flights* rows are leaving out of it. It's like making the connection two-ways.

<br>

#### More Explanation on Related Name
`flight.origin` gives us the airport. But what if we want to do the reverse and find all the flights going out of an airport? If we set `related_name="departures"`, that will let us run `airport.departures` to get all flights connected to that airport.

Or well, technically we would run `jfk.departures.all()` to get all of the departures. Idk what would happen if you just do `jfk.departures`.

<br>

#### ***on_delete** Options
1)  `models.CASCADE`: if an `Airport` gets deleted, the corresponding `Flight` will also be deleted.
2) `models.PROTECT`: does not allow us to delete an  `AIRPORT` if it is connected to a `FLIGHT`.

NOTE ON FOREIGN KEYS:
Sometimes when creating new fields in models, we can come across this error:
`You are trying to add a non-nullable field 'highestBidder' to listing without a default; we can't do that (the database needs something to populate existing rows).`
It's a pretty clear error. You are trying to create a field, that can't be null, without giving it a default. Django doesn't like this because what kind of value is it going to give the field? The way around this I have found is simply giving it a default of 0:
`highestBidder = models.ForeignKey(User, default=0, on_delete=models.CASCADE)`

I *think* this works okay because Django seems to start IDs from 1, almost as if it set aside '0' for us to use.

#### Defaults/Nullability
By default, a foreignkey is allowed to be `null` or `blank`. You would have to forbid these states explicitly if you wanted them.

------

<br>

### ManyToMany relationships
Say we have Flights and Passengers, can't we just create a Flight relationship with Passengers, like this?

```python
Passenger(models.Model):
	flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="upcomingFlights")
```

This is fine...except that sometimes you need to transfer airports, and then you will have to link a Passenger to *more than one* flight.

Becuase a passenger can have many flights and a flight will have many passengers, this is a *many to many relationship*.

As we've seen above, a many-to-many relationship cannot just be handled by a single foreign key between two tables. It requires us to create a *third* table, in which we track all of the relationships between two other tables. We can add as many of these relationships as we want. I suppose we could also use this method to track relationships between more than two tables as well.

Django actually abstracts the hell out of this, and allows us to simply express this with a different kind of field, which is aptly named:

```
Passenger(models.Model):
	flights = models.ManyToManyField(Flight, blank=true, related_name="passengers")
```

Looks pretty similar to a `ForeignKey` type field, but it's different. The options look the same, except for `blank=true`, which just means that this passenger *could* have *no* flights associated with them.

Django is actually creating a many-to-many table *for* us here in SQL, behind the scenes, but we don't need to worry about it which is nice.

#### Nullability and Jank

If you want to be able to specify ManyToMany relation without making it required just use `blank=True`:  ManyToMany can't be null, but they can be blank.

<br>

---

<br>

### Non-Nullable Fields Errors
Are you getting a message like this?

```
You are trying to add a non-nullable field 'highestBidder' to listing without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
```

You may need to add a `null=True` option into your model.

This also may just mean that you have rows in your database for which a new field will be added, and Django needs you to tell it the default, either a "null" by entering '1' or a default value entered in the model, by entering '2'. If adding a default value isn't any option for you here, you may have to delete rows in your database to keep from creating errors in it.
<br>

---

<br>

### New Model Checklist
Every time you create a model, you'll probably have to do all of the following:
1. Make a new migration
2. Apply the migration
3. 'Register' the model in your admin app if you want to be able to use it in your admin interface.







<br> 

---


<br>



# Interacting with Database

### Views.py
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

----

<br>

### HTML Templates
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


<br>

-----


<br>


### Adding Data
1) In `urls.py`, add a path for `path("<int:flight_id>/book", views.book, name="book")`
2) Implement the method in `views.py`:

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
 
 <br>


------
 
 
 <br>
 

# Using the Admin App

Run this:

```shell
python manage.py createsuperuser
```

add username and password. Getting an error? It might be a problem with your database. Check out the migrations section.

Now you will need to 'register' the models you want to show up in the admin app. You do this in the `admin.py` file inside of your app. Don't forget to import them first:

```python
# app/admin.py

from .models import User, Listing

admin.site.register(User)
admin.site.register(Listing)
```



 
 ### Accessing table data from Views.py
 We're probably going to be doing this is in the  `views.py` file. We can just access these sort of globally. Within any `def` we can just say stuff along these lines:
 `Flight.objects.get(pk=flight_id)` get a flight with a particular flight_id
 `Passenger.objects.exclude(flight=flight).all()`Get all passengers EXCEPT FOR ones that already have flights (note: in this case, we are using a variable `flight`, which could have been the result of the first query)
`Flight.objects.all()` Get all  flights.

<br>

---

<br>
<br>
<br>

# Questions Section

#### 1) What actually calls the `__str__` function?
I guess it's Django, returning some value generated, and we're possibly creating an overload for it or something like?

<br>

### 2) Foreign Keys are not strings...?
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

<br>

### 3) Weirdness of importing stuff in the Django shell
Yeah wait, so when I use the django shell I need to import stuff everytime? Let me just point this out because I can see how if I forgot, it would be a pain in the ass realizing this since I'm not at all used to importing things in a shell for temporary use. So that syntax looks like this:
`from flights.models import *`
We used it before a few times. So just remember that. You gotta import stuff before using the shell.