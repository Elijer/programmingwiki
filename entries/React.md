# Paradigm
React is a type of "declarative" programming, as opposed to 'imperative' programming.

# Basic packages needed for react
1. React: library that defines components
2. ReactDOM: inserts React Components into DOM
3. Babel: translates JSX into normal JS 

# Basic, Fast Boilerplate:
Note -- the script tags aren't legit. They are placeholders. You'll have to get the actual URLs for these packages.

```HTML
<!DOCTYPE html>
<html>
	<html lang="en">
	<head>
		<script src = "react"></script>
		<script src = "react-dom"></script>
		<script src = "babel"></script>
	<head>
	<body>
	
		<div id = "app"></div>
		
		<script type = "text/babel">
			function App() {
				return (
					<Hello name = "Elijah" />
					<Hello name = "Katie" />
					<Hello name = "Pooyan" />
				)
			}
			
			function Hello(props){
				return (
					<div> Hello, {props.name} !</div>
				)
			}

			ReactDOM.render(<App />, document.querySelection("#app"));
			
		</script>
		
	</body>
</html>
```
	
In production, the babel translation should be done ahead of time, but for development, we can translate it as it runs.

# State

```HTML
<!DOCTYPE html>
<html>
	<html lang="en">
	<head>
		<script src = "react"></script>
		<script src = "react-dom"></script>
		<script src = "babel"></script>
	<head>
	<body>
	
		<div id = "app"></div>
		
		<script type = "text/babel">
		
			function App() {
				const [count, setCount] = React.useState(0);
				
				function updateCount() {
					setCount(count + 1)
				}
				
				return (
					
					<div>
						<div>  {count} </div>
						<button onClick = {updateCount} >Count</button>
					</div>
				)
			}

			ReactDOM.render(<App />, document.querySelection("#app"));
			
		</script>
		
	</body>
</html>
```

### The useState() Function `useState()`
```javascript
const [count, setCount] = React.useState(0)
```

This inputs `0` as single argument to the use state function.  I haven't quite wrapped my head around it, but the way the useState function returns a value is actually sort of backwards, with a destructuring assignment (again, I still don't totally understand these).

It's like I am passing in empty variables called `count` and `setCount` to be properties OF a...method? That's the part that's weird to me. If it was just `React.useState`, and that was an object in itself, that would make sense. But `useState` is a function, a method.

Which leads to a question; am I adding `count` and `setCount` as parameters of the function itself (not something I knew that was possible tbh) OR am I adding them as parameters to an object that useState() returns? The second one makes more sense, and seems possible.

It depends -- in a destructuring assignment, is the thing on the right of the `=` operator a reference or an actual value?

I guess I don't really need ot know the answers to these questions because it basically resembles `out` variables in C#.

So first we add count and setCount as properties of React's use state.

So now that we have this line: 

```javascript
const [count, setCount] = React.useState(0)
```

we can use this variable `count` like this:
`<div> {count} </div>`

But we can't *change* the count. We have to use the `setCount` function we were provided:

And we can use the setCount variable like this:

```setCount(count +1)```

It's sort of like a setter or, whereas `count` is the getter.

So I'm guessing that when you run the desctructuring assignment, the getter is always the first one, and the setter is always the second one. Let's break that down more graphically:

```javascript
const [getter, setter] = React.useState(0);
```

Basically it has three parts -- the getter, the setter, and the starting value.

Okay, so what if I want multiple state variables? Well, we can plausibly just repeat it with different getters and setters:

```javascript
const [getter1, setter1] = React.useState(0);
const [getter2, setter2] = React.useState(0);
```

This works! But there's a better way to do it by maintaining state into a single javascript object.

```javascript
const [state, setState] = React.useState({
	num1: 1,
	num2: 2
})

<div> {state.num1}, {state.num2} </div>
```

And we can keep going:
```javascript
const [state, setState] = React.useState({
	num1: 1,
	num2: 2,
	response: ""
})
```

How do we use state with textfields? Not like this:
```html
<input value = {state.response} />
```

We can't do this, because this means no matter what the user enters as a value, it will always be replaced by whatever is in `state.response`, so quickly in fact, it will basically appear to the user as if the input isn't even working.

How to fix this? We need to make sure that an input event changes the state BEFORE the the input field's value changes. Let's create an event handler:

```
function updateResponse(event){
	setState({
		response: event.target.value
	})
}
```

Ah but shit if we do this, it will actually rewrite the entire state, getting rid of num1 and num2. But we don't want to have to write out num1 and num2 everytime we change the response.

There's a built-in solution in javascript though, which is the `spread operator.`

```javascript
setState({
	...state,
	response: event.target.value
})
```

This tells JS that we want to keep the javascript object as it is EXCEPT for whatever parameter we are changing.

# Allowing State to interact with CSS
```javascript
<div className = {state.incorrect ? "incorrect" : ""}
```

This is a cool way to set the class using state and a terniary operatory.