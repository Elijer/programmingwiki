# I have a dream
I really just want to use ES6 modules and other features in a simple, otherwise vanilla js project without a framework, AND JSX to do all of the HTML templating. But it's crazy. They say you can use JSX without React, but it doesn't seem that easy to me. Let's give it a shot. [This blog post seems to offer the simplest explanation.](https://betterprogramming.pub/how-to-use-jsx-without-react-21d23346e5dc)

# Pragmas
Wtf is a pragma? Turns out it is just a line of code, in this case actually a *commented out* line of code, that instructs a bundler to use a different function to transpile a certain type of synstax. Seems crazy specific and niche. Whatever. So in this case, our pragma is this:

`/** @jsx myJsxFunction */`

It's saying *'in this file, for jsx, use the functioned named ' myJsxFunction' to transpile the code instead of whatever tf you would normally use, okay?*

You just slap this at the top of your file. No, I don't know why it has double asterisks.

*Now*, Babel (for example - I guess you could use another transpiler? I don't actually know of any others) will pass the parameters to your function instead of, in this case, React.createElement, which is the default for JSX. We don't want to use React at all in this project, so let's tell it not to do that!

# Our own transpiler function
First off, where do we put this? Well, this is what we start with:

```javascript
export const createElement = (tag, props, ...children) => {
	const element = document.createElement(tag)
return element
}
```

And it's an export. So I guess we can just export it from our main js file in our `src` folder? Then it should be globally available and idk where babel would be able to access it if not there. Just a guess. This tutorial unfortunately doesn't say.