# Python

Python is a programming language that can be used both for writing **command-line scripts** or building **web applications**.

## Characteristics of Python
File extension is `.py`

Python is an interpreted language, which means that a program called Python is needed to run `.py` files. The interace for using the Python profile is the CLI keyword `python`. A basic example of this is running the pythong file `hello.py` by running `python hello.py` in the command line.

Python is interpretive, which means that types do not need to be explicitly defined. These are the types:

int, float, str, bool, noneType

Everything here is familiar from a background in JS, except for possibly the `NoneType`.




## Basic Usage

`print("")`

`name = input("This is the prompt")`

`f"string {logic}"`

By putting f in front of a string you can use logic in curly braces inside of the string.

The '#' character works the same as // (in js) in order to comment a line out. I think that tripple backticks are multi-line comments

## Conditionals

```
if n > 0:
    print("test")
```

Conditionals are expressed with a colon and indentation. The else if syntax looks like this:

```
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
`things = ["thingy", "thingy", "thingette"]`
`thingOne = things[1]`


tuple
Sequence of immutable values
`tuple = (1, 2)`

set
Sets don't keep thing in any order, and every value must be unique.

dict
A collection of key-value pairs, also not ordered.

## Lists
#### Appending
list.append("newthingy");

#### Sorting
`list.sort()`
presumably takes arguments to print things differently.

#### Sets
```
s = set()
s.add(3)
s.remove(3)
# calculates the length of the set
len(s)
```

## For Loop

```
for i in list:
    print(i)
```

If you don't have a list and don't want to write one, you can use range()

```
for i in range(6)
    print(i)
```

## Dictionaries

`houses = {"harry": "gryffindor", "draco":"slytherin"}`
So yeah, commas and colons and quotes. Accessing or adding data to an existing set:
`print(houses["Harry"])`
`houses["Hermione"]="Gryffindor"`

## Functions
```
def square(x):
    return x * x
```

## Importing/Exporting things
Define a function in one file, and then call it in another file, do this:
`from functions import square`,
where functions is the file name and square is the variable.
You can also do this:
`import functions`
and import all of the variables in a file/module, but then accessing the variables is different:
`functions.square`
You have to use dot notation like that. So you can import all sorts of import modules from Python itself I think.
You can also install functions other people make and then import them. Which has something to do with Django.

### OOP in Python
##### Basic Class
Python has several types, if you want to create a new one, you use the class keyword.

```
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

```
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

```
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
```
people = [
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Harry", "house":"Gryffindor"}
]

people.sort()
print(people)
```
If you try to do this (imagine each entry in the dict is different), you will get an error, '<' not supported between dict and dict.

```
def f(person):
    return person["name"];

people.sort(key=f)
```

This is how you tell sort how to sort a dict. Or well sort of. There is an easier way to do it because I guess it's a common thing. Instead of `def f(person)`, I can do this:

`people.sort(key=lambda person: person["name"])`

It's a sort of shorthand.

## Setting up Environment
Still learning about this, but apparently you don't want to just run a global instance of Python from your path. You want an intermediary running python for you that allows you to run different versions of python for different projects, and even set up different package environements. From my understanding there are a few different options:

1. Pip: Not a version manager, but the package manager python uses
2. Pyenv: a python version manager that helps you use different releases of python with different projects
3. Anacanda: a heavier and more sophisticated tool that seems to generally be used by data scientists more, allowing you to create different package environments (I think) and also giving you access to some very sophisticated scientifically-oriented packages. A python web developer on stack overflow said he hadn't used anaconda.

[Explanation of this confusion](https://opensource.com/article/19/5/python-3-default-mac) and what to do about it.

[More about it on stack overlflow.](https://stackoverflow.com/questions/38217545/what-is-the-difference-between-pyenv-virtualenv-anaconda)

[How to use pyenv to run different versions of python on your mac.](https://opensource.com/article/20/4/pyenv)


# Useful Packages

[Markdown2](https://github.com/trentm/python-markdown2)