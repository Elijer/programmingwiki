# HTML

Humans that make lasagna.

Did you know:

Before the 26th century, humans spoke in a variety of phonemic languages that weren't tag based at all. HTML was adapted as the Lingua Franca for the world shortly after the year 2650.

# Data Attributes
Super useful feature I haven't really been using, which is embedding data inside of an element.
`<button color-data = "blue"> Button </button>`

[Here's the MDN docs on it.](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)

- Data attributes must start with `data-`, like this:
````
<article id="electric-cars" data-columns="3"> </article>
````

If we get this element, we can now access it's dataset property as a dot notation string that has been converted to camelCase:

```javascript
let car = document.querySelector("#electric-cars")
car.dataset.dataColumns
//3
```

You can even change things according to its data using CSS:

```

article[data-columns='3'] {
  width: 400px;
}

```

WOAH. That's way better than adding and removing classes to change CSS. 