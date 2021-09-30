# Javascript

The language that web browsers parse in order to add logic to websites. Serverside rendering can be powerful, but so can clientside

If you wanted to contrast this with Django, it looks like this: whenever you want to change or edit data in a webpage served by Django, you have to revresh the page because you are actually getting a file form the server.

The big whoop with javascript? It's not complicated: you don't need to reload the page. That's pretty much it.

<br>

----

<br>

# Using the Javascript Console
Definitely do this! You can modify variables, run functions, run document.querySelector, see what the values of variables are, etc. Super great debugging tool, and faster than checking these things in an IDE.

<br>

----

<br>

# The Script Tag
Can be included in the head or the body of an html file.

<br>

----

<br>

# Event Driven Programming
It's possible to add "listeners" to a web-page in a way that isn't really possible with other languages. Because JS is what the browser uses, Javascript can *interrupt* the browser processes with code you want conneted to an event you've specified.

<br>

----

<br>

# DOM Lifecycle / Events
- **DOMContentLoaded**:  DOM is ready, so the handler can lookup DOM nodes, initialize the interface.
- **load**: Not only HTML is loaded, but also all external resources; image, style, etc.
- **beforeunload/unload**: The user is leaving the page.

Autofill: Browser's usually autofill things on **DOMContentLoaded.**

**window.onload**: Not really sure how this is different than the **load** event.
**window.onunload**: Likewise, not sure how this is different than the **unload** event.

**document.readyState**: This tells us what state our page is in -  has the DOM loaded? The resources? It can have these states:

-   `"loading"` – the document is loading.
-   `"interactive"` – the document was fully read.
-   `"complete"` – the document was fully read and all resources (like images) are loaded too.

<br>

----

<br>

# Manipulating the DOM
```javascript
var someDiv = document.createElement('div')`
document.querySelector("target").append(someDiv)
```

<br>

----

<br>

# HTTP in JS
### 'Fetch' function
Fetch is an asynchronous function built into modern JS that allow you to make HTTP requests. Example:

```
fetch('/emails/inbox')
.then(response => response.json())
.then(emails => {
    // Print emails
    console.log(emails);

    // ... do something else with emails ...
});
```

<br>

----

<br>

# Variables
`const`
will never change


`var` and `let`
can change

Then how are `var` and `let` different?

`var` is function scoped nad `let` is block scoped.

<br>

----

<br>

# Interacting with the DOM
`document.getElementByID("id")`

`document.querySelector('h1')`

<br>

----

<br>

# Functions
1) 
```var func = function(){
}
```
2) 
```function func(){
}
```


<br>

----

<br>

# Arrow Functions `=>`
Arrow functions `argument => body of function;` are a compact alternative to traditional function expressions, but have limitations and can't be used in all situations.

Limitations:
- Does not have it's own binding to `this` or `super`, and should not be used as methods.

<br>

----

<br>

# This Keyword `This` 
Supposedly behaves differently than in some other programming languages. It also has some differences between strict-mode and non strict-mode.

It can be very confusing. Hopefully [this article breaks it down.](https://dev.to/chuckchoiboi/is-this-really-that-complicated-in-javascript-4o3h). Some excerpts:

'To put it simply, `this` is a keyword used to reference the execution context.'' That context may the global context, it may be a function or another code-block, it may be an object.

`this` behaves differently, though, if it is invoked by an arrow function OR if you are using strict mode.

A simple way to look at it is that whatever is on the left side of a dot notation of a method being invoked is the object that `this` will be referring to. Consider this block then:

```
  function whatIsThis() {
    console.log(this);
  }

  whatIsThis(); // prints Window {...}
```

There's nothing to the left of the fuction being called. Not at first glance anyways. Technically though, eveything we write in javascript is in the scope of the `window` object, which is the global context of the browser. That's why the Window object gets printed! To demystify further, we can say that the last line of the code block above is the same as calling the following function:

`window.whatIsThis()`

To go even further with the concept, let's print the following line:

```
  console.log(this); 
```

This line will print the same result of: `Window {...}`

Another super simple way to think of `this` when we are using event listeners is that `this` just refers to the element who called/recieved the event. If it's an `onclick` handler for a button, then `this` will refer to that button.

<br>

----

<br>

# The Window Object
The window object is the Global Object in the Browser. **Any Global Variables or Functions can be accessed as properties of the window object.**

<br>

----

<br>

# Strict Mode
This is not the default mode. It is pretty much what it says. Javascriopt is a very flexible language, and strict mode enforces an extra layer of, well, strictness. It throws errors that otherwise would be silent and is less forgiving with things like `type errors` (I would assume. I don't actually know as I have never used it).

To invoke strict mode for an entire script, put the _exact_ statement `"use strict";`before any other statements.

<br>

----

<br>

# Destructuring Assignment
Declaring variables inside of curly brackets like this:

```javascript
{x, y} = foo;
```

Which is roughly equivalent to:

```javascript
x = foo.x;
y = foo.y;
```

Although, someone mentioned that a more real-world example might be this:
```javascript
{width, height, color} = options
```

In my experience though, the situation where it is indispensable is when you add an object as a parameter of some function, and then you want to add a property to that object within the function. I don't think you can do this any other way. But with a destruturing assignment, you can!

```javascript
function(someObject){
	{ newProperty } = someObject
	return someObject
}
```

This function has the ability to add a property to an object. I don't know *why* you would have to do this, but sometimes you gotta do word stuff.

[This stackoverflow answer breaks it down pretty well.](https://stackoverflow.com/questions/25187903/what-do-curly-braces-around-javascript-variable-name-mean)

<br>

----

<br>

# Local Storage
```javascript
localStorage.setItem("moose", "A moose is a wonderful animal")

localStorage.getItem("moose")
// A moose is a wonderful animal
```

There is also a section of the javascript inspector that shows you all current localStorage entries.

<br>

----

<br>

# Javascript objects

```javascript

var person = {
	first: "Harry",
	last: "Potter"
}

person.first
// Harry

person["first"]
// Harry

var str = "first"
person[str]
// Harry

```

# The Spread Operator
Sometimes, when using objects in JS, you will come into a problem that looks like this:
```javascript
var someObject = {
	str1: "This is a pretty complicated object",
	explanation: {
		p1: "it just has a lot of",
		p2: "different parts"
	},
	conclusion: "and if we want to update multiple parts of it, it could be tricky."
}
```

It's not really that bad. We can still update it by doing this:

```javascript
someObject.explanation.p1 = "It just has a lot of"
someObject.explanation.p2 = "different PARTS."
someObject.conclusion: "And if..."
```

Which is aight. But it's verbose. There's a nicer way:

```javascript
someObject = {
	...someObject,
	explanation: {
		p1: "whatever",
		p2: ""
	}
}
```

This `...someObject` is called the spread operator, and it is an ellipses followed by the object that you want to 'fill in the cracks' of your current object with. In this case, we are using the same object. It says, everything should stay the same except for whatever parameters I am defining.

You may never have to use this. It is, however, useful in setting state in the React framework.

<br>

----

<br>

# Fetch

```javascript
fetch('https://someurl.api.io')
```

Returns a promise:

```javascript
fetch('https://someurl.api.io')
.then(response => response.json())
```

Woah -- so now we have some JSON data from an API! Let's do something with it.

```javascript
fetch('https://someurl.api.io')
.then(response => response.json())
.then(data => {
	console.log(data)
})
```

Dooope. So this will print a javascript object to the console. And since it's a javascript object, we can do:

```javascript
console.log(data.someField)
```

Of course, sometimes when we try to fetch something, it won't work. So we can add a catch case:

```javascript
fetch('https://someurl.api.io')
.then(response => response.json())
.then(data => {
	console.log(data)
})
.catch(error => {
	console.log(error)
})
```

<br>

----

<br>

# Null vs. Undefined vs. ""
What is the difference??? I !know.

<br>

----

<br>
 

# Single-Page Applications
Single page applications is a modern web design paradigm. It means creating a web page that doesn't require refreshing the page or using HTTP routes in order to update the renering of data.

This is done by advanced manipulation of the DOM. It's popular because it's faster and leads to a better user experience.

##### Not loading the entire website for each page though
We can do this by fetching new data for each page. Sounds kind of weird though, right? It's like, we're going through all this effort to *not* have multipage HTTP driven sites, but then we're still using the same stuff. We're just avoiding that refresh.

- Gained: better load times in efficiently loading what you want to change instead of the entire page
- Lost: url organization, that's bookamarkable and stuff

But for the URL organization stuff, we can simulate that kinda it sounds like.

# Simulating URL Routing

1)

**history.pushState(data, title,  url_string)**
Adds a new element to the browsing history.
```javascript
let str = "want"
history.pushState({data: someData}, "", `theURLI${str}`);
```

2)

**window.onpopstate**
This tells the browser what to do when the user presses the back button. You need to record state in order to do this though. Don't really know how to do that yet.
```javascript
// when you go back in the history
window.onpopstate = function(event){
	showSection(event.state.section)
	// do something
}
```

3)

I think there's still something missing though, right? Because we can't get the right data just by going to the urls that we're pushing to our history.

<br>

----

<br>

# The Window Object
What is the window object? It's sort of everything. Here are some useful properties

`window.innerWidth`
How wide is the window?

`window.innerHeight`
How high is the window?

`window.scrollY`
How many pixels down have I scrolled?

`window.onscroll`
This is run when the user scrolls.


<br>

----

<br>

# The Document Object
The document doesn't always fit inside of the window, but the data is still ready to be rendered.

`document.body.offsetHeight`
How tall is the entire document