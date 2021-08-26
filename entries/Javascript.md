# Javascript

The language that web browsers parse in order to add logic to websites.

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


# Arrow Functions `=>`
Arrow functions `argument => body of function;` are a compact alternative to traditional function expressions, but have limitations and can't be used in all situations.

Limitations:
- Does not have it's own binding to `this` or `super`, and should not be used as methods.

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

# The Window Object
The window object is the Global Object in the Browser. **Any Global Variables or Functions can be accessed as properties of the window object.**

# Strict Mode
This is not the default mode. It is pretty much what it says. Javascriopt is a very flexible language, and strict mode enforces an extra layer of, well, strictness. It throws errors that otherwise would be silent and is less forgiving with things like `type errors` (I would assume. I don't actually know as I have never used it).

To invoke strict mode for an entire script, put the _exact_ statement `"use strict";`before any other statements.

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