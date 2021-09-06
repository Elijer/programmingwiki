# Python

Python is a programming language that can be used both for writing **command-line scripts** or building **web applications**.

## Characteristics of Python
File extension is `.py`

Python is an interpreted language, which means that a program called Python is needed to run `.py` files. The interace for using the Python profile is the CLI keyword `python`. A basic example of this is running the pythong file `hello.py` by running `python hello.py` in the command line.

Python is interpretive, which means that types do not need to be explicitly defined. These are the types:

int, float, str, bool, noneType

Everything here is familiar from a background in JS, except for possibly the `NoneType`.




## Basic Usage

```python
print("")
name = input("This is the prompt")`
f"string {logic}"
```

By putting f in front of a string you can use logic in curly braces inside of the string.

The '#' character works the same as // (in js) in order to comment a line out. I think that tripple backticks are multi-line comments

## Conditionals

```python
if n > 0:
    print("test")
```

Conditionals are expressed with a colon and indentation. The else if syntax looks like this:

```python
if something
    do something
elif somethingElse
    do something else
else
    do yet another thing
```

## Data Structures

lists
sequence of MUTABLE values
```python
things = ["thingy", "thingy", "thingette"]
thingOne = things[1]
```


tuple
Sequence of immutable values
```python
tuple = (1, 2)
```

set
Sets don't keep thing in any order, and every value must be unique.

dict
A collection of key-value pairs, also not ordered.

## Lists
#### Appending
list.append("newthingy");

#### Sorting
```python
list.sort()
```
presumably takes arguments to print things differently.

#### Sets
```python
s = set()
s.add(3)
s.remove(3)
# calculates the length of the set
len(s)
```

## For Loop

```python
for i in list:
    print(i)
```

If you don't have a list and don't want to write one, you can use range()

```python
for i in range(6)
    print(i)
```

## Dictionaries

```python
houses = {"harry": "gryffindor", "draco":"slytherin"}
```
So yeah, commas and colons and quotes. Accessing or adding data to an existing set:
```python
print(houses["Harry"])
houses["Hermione"]="Gryffindor"
```

## Functions
```python
def square(x):
    return x * x
```

## Importing/Exporting things
Define a function in one file, and then call it in another file, do this:
```python
from functions import square
```,
where functions is the file name and square is the variable.
You can also do this:
```python
import functions
```
and import all of the variables in a file/module, but then accessing the variables is different:
```python
functions.square
```
You have to use dot notation like that. So you can import all sorts of import modules from Python itself I think.
You can also install functions other people make and then import them. Which has something to do with Django.

### OOP in Python
##### Basic Class
Python has several types, if you want to create a new one, you use the class keyword.

```python
class Point();
    def __init__(self, x, y):
        self.x = input1
        self.y = input2
p = Point(2, 8)
print(p.x);
printp.y
```

Beautiful. It has some weird stuff, but nothing that doesn't make sense. Like, I don't know WHY class creation needs to work this way, but it's pretty intuitive.

##### Underscore underscore init nderscore underscore
Brian calls this a 'magic method', probably because you're not supposed to know how it works. The first argument represents self, whatever you call it, and the proceeding arguments are taken as constructor arguments

##### A more self-referential and complex class

```python
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self)
        return self.capacity - len(self.passengers)
flight = Flight(3)
people  = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person)
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
```

## Decorators
Decorators take functions as arguments and then they return a modified version of the function.
They belong more to the functional programming paradigm.

```python
def announce(f):
    def wrapper();
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("hello")
```

## Lambda
```python
people = [
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Harry", "house":"Gryffindor"}
]

people.sort()
print(people)
```
If you try to do this (imagine each entry in the dict is different), you will get an error, '<' not supported between dict and dict.

```python
def f(person):
    return person["name"];

people.sort(key=f)
```

This is how you tell sort how to sort a dict. Or well sort of. There is an easier way to do it because I guess it's a common thing. Instead of `def f(person)`, I can do this:

```python
people.sort(key=lambda person: person["name"])
```

It's a sort of shorthand.

### Try/Except

The `try` block lets you test a block of code for errors.
The `except` block lets you handle the error.
The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

Normally in python when an error happens (or an *exception* as it is sometimes called)
, python will stop altogether and generate an error message.

With the `try` statement, these errors/excepts can be handled, presumably in cases when errors are expected and unavoidable, although hopefully rare.

Here's an example. `try` will not succeed, as x is not defined.

```python
try:  
 print(x)  
except:  
 print("An exception occurred")
```

But the program will keep going and do whatever you tell it to do if there *is* an error. In this case, we print a line to the console. But we might send an email alerting developers that something isn't right, or cancel a transaction, etc. If we *just* ran the iffy code without the `try/except` blocks, like so:

```python
print(x)
```

Then the program will crash. A much worse scenario! We can avoid it with `try/except` :)

I think we can be more specific though, as there are, alas, many types of errors. Here's an example of how specific errors can be handled in a different way than general errors:

```python
try:  
 print(x)  
except NameError:  
 print("Variable x is not defined")  
except:  
 print("Something else went wrong")
```

How do we know that a `NameError` might occur? I guess by breaking the program to begin with! If you're not breaking your program you're not discovering the edge cases. If you discover the edge cases and the errors they may cause, *then* you can start handling exceptions.

**Else**

We can also add an `else` block for when there are no errors.

```python
ry:  
 print("Hello")  
except:  
 print("Something went wrong")  
else:  
 print("Nothing went wrong")
```

**finally**

We can also run this block, appropriately enough after everything else, which contains code that will run regardless of whether there were errors or not.

### Raising our own errors! `raise`
We can use the `raise` keyword to raise our own errors. This is how it's done:
```python
x = -1  
  
if x < 0:  
 raise Exception("Sorry, no numbers below zero")
```

We can be more specific than `exception` if we would like:

```python
x = "hello"  
  
if not type(x) is int:  
 raise TypeError("Only integers are allowed")
 ```

## Setting up Environment
You don't want to just run a global instance of Python from your path. This can cause all sorts of issues, since (for Mac) your OS also relies on the global instance of Python. If you try and install packages to the global instance, you'll find that they'll usually get lost. 

You need an intermediary running python for you that allows you to run different versions of python for different projects, and even set up different package environements. From my understanding there are a few different options:

1. Pip: Not a version manager, but the package manager python uses
2. Pyenv: a python version manager that helps you use different releases of python with different projects
3. Anacanda: a heavier and more sophisticated tool that seems to generally be used by data scientists more, allowing you to create different package environments (I think) and also giving you access to some very sophisticated scientifically-oriented packages. A python web developer on stack overflow said he hadn't used anaconda.

[Explanation of this confusion](https://opensource.com/article/19/5/python-3-default-mac) and what to do about it.

[More about it on stack overlflow.](https://stackoverflow.com/questions/38217545/what-is-the-difference-between-pyenv-virtualenv-anaconda)

[How to use pyenv to run different versions of python on your mac.](https://opensource.com/article/20/4/pyenv)

This has become especially problematic as Python 2.X has been deprecated, since some deprecated tools/software still rely on Python 2, but anything new being built should use Python 3. Without properly installing an intermediary python environment, you'll also find that the packages you install are installed into a void! For that reason, anything other than vanilla Python is pretty much impossible to use without an intermediary python environment.

The easiest quick-start to Python that Noah has found has been Pyenv. 

At the time of writing, these were the steps - 

1. Download and install Pyenv through Homebrew (Note that both pyenv and pyenv-virtualenv are required). 
```
brew update
brew install pyenv
brew install pyenv-virtualenv
```

2. Set-up Pyenv through your environment variables (PATH, etc) so that your computer knows how to reach Pyenv. This is different for `bash` and `zsh`, but luckily the [`pyenv` documentation on their `README` is pretty good.](https://github.com/pyenv/pyenv#installation). 
> Note that the documentation is extremely verbose. Read carefully and be patient. If you followed the above steps for Homebrew, Skip to Installation/2. Configure your shell's environment for Pyenv. Make sure to follow both steps, i) and ii). 

3. Restart your terminal AND your IDE for the changes to take effect. 

4. Run `pyenv install x.x.x` to install the version, where `x.x.x` is your version number. Version `3.7.2` is stable and recommended at time of writing. 

5. [See here for a great guide on `pyenv` basic usage](https://gist.github.com/josemarimanio/9e0c177c90dee97808bad163587e80f8#basic-usage)


## Pass keyword `pass`
We can use this to execute...nothing. This can be useful when we have written a function declaration but not the function, since python is shit at commenting things out.

# Useful Packages

[Markdown2](https://github.com/trentm/python-markdown2)
