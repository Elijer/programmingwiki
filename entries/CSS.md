# CSS

CSS is a language that can be used to add style to an [HTML](../pages/HTML) page. It is an acronym that stands for "Cascading Style Sheets", which was clearly termed in the late 80's when everything was rainbows and cocaine until the end of the dot com boom. The creator of CSS is rumored to have been listening to TLC "Don't Go Chasing Waterfalls" when she invented it.

Cool. Seriously cool.

<br>

-----

<br>

# Grid

**Go-to CSS Grid Learning Resources**

- [CSS Trick's "A Complete Guide to Grid"](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [MDN 'Basic Concepts of Grid Layout' ](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout)
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)

So powerful! So...alien. I've used this many times and I *still* didn't get it for the longest time.

A simple, very common usage case: 

```css
#listing-grid{
	display: grid;
	grid-template-columns: repeat(4, 1fr);
}
```

What's happening here?

1) We are styling a *container* element. This elements children will be the tiles or boxes or whatever is in your grid.
2) `display: grid`. This is what tells css, we're using grid! Not normal inline or block display. There is also `display: inline-grid`, but I dunno much about it.
3) `grid-template-columns` If you want to have a certain number of columns in your grid, this is the property you are going to define next. It tells CSS how big you want your columns to be. Alternatively, you could use `grid-template-rows` if it's more important to you to have a certain number or rows. Can you use both together? Not sure.
4) `repeat` This is a sort of css function that takes two arguments. The first is how many times you want to repeat something, and the second is a size. To understand this, we should probably look at how you would define your column sizes *without* repeat.
5) `grid-template-columns: 1f 1fr 1fr 1fr;` This is the same as using repeat like this: `repeat(4, 1fr)`, but it's more DRY.
6) What is a `fr` ? It's short for 'fraction'. It's actually brilliant. If you have this: `1fr`, then it basically stands for 1/1 of the available horizontal space. But if you have `1fr 1fr`, then each one is 1/2 of the available space. `1fr 1fr 1fr 1fr` identifies 4 sizes that are each 1/4th of the available space! It's nice cause then we don't need to do the math ourselves each time the available space changes. But we could if we wanted to, and us other units of measurement instead: `grid-template-columns: 100px 4em 4% 20pt`
7) As you can see, we don't have to supply the `grid-template-columns` property with equal portions either. Normally when I think of a grid I think of equally spaced rows, but CSS grid is more flexible than that. We probably want to use fractions again though, to do something like this: `grid-template-columns: 1fr 1fr 4fr 2fr`. We just defined some rows with clear yet unequally sized columns.

<br> 

---

<br>


# Styling Images (IMG)
Images are weird. At least when you select your own images as a developer, you know their dimensions. However, if images are supplied by the user, you may struggle to control the formatting of the image to handle all cases, mostly the range of image size and aspect ratio.

**Solution 1:**
This solution constrains the width *and* constrains the height *while* keeping the aspect ratio. How? Additional height is redirected out of what is displayed. I think you want to do this in *addition* to specifying the width of the image in the HTML, otherwise you will get all sorts of widths.

*HTML*
```HTML
<img src="..." width="300px">
```

*CSS*
```css
img {
	object-fit: cover;
	width: 100%;
	height: 250px;
}
```

This approach seems to work really well with CSS grid.


#### Properties to note:
```css
object-fit: cover;
width: 100%;
height: 250px;
display: block;
max-width:230px;
max-height:95px;
width: auto;
height: auto;
```

<br> 
#### Links
- [CSS force image resize and keep aspect ratio](https://stackoverflow.com/questions/12991351/css-force-image-resize-and-keep-aspect-ratio)


<br> 

---

<br>


# Inline Elements
Can't be given vertical margins! Only horizontal ones.

<br> 

---

<br>

# Animations
```css

@keyframes grow {
	from {
		font-size: 20px;
	}
	
	to {
		font-size: 100px;
}


h1 {
	animation-name: grow;
	animation-duration: 2s;
	animation-fill-mode: forwards;
	
}
```

We can do `from` and `to`, but we can add other keyframes if we want too! We can use percentages.

```css

keyframes move {
	0% {
		left: 0%;
	}
	
	50% {
		left: 50%;
	}
	
	100% {
		left: 0%;
	}
}

```

We can also repeat animations with `animation-iteration-count`:

```css

@keyframes grow {
	from {
		font-size: 20px;
	}
	
	to {
		font-size: 100px;
}


h1 {
	animation-name: grow;
	animation-duration: 2s;
	animation-fill-mode: forwards;
	animation-iteration-count: 2;
}
```

And if you want you can set `animation-iteration-count:` to `infinite` if you don't want it to ever stop.

And of course you can use javasript to control the animations as well.

```javascript
document.addEventLister('DOMContentLoaded, function(){
	const el = document.querySelector('h1');
	el.style.animationPlayState = 'paused'
}')

some listener {
	if (el.style.animationPlayState === 'paused'){
		el.style.animationPlayState === "running";
	} else {=  
		el.style.animationPlayState === "running";
	}
}
```

Okay question: everything else pretty much makes sense, but what is this animation fill mode property?

[Here's a link to MDN for that.](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-fill-mode)

It seems to basically tell our element what to do when the animation *isn't* happening. Consider this - you tell an element to move from square one to square 4 in 2 seconds. Once it's done, where will it be? That's what `animation-fill-mode` is for.

Here are our options for it:
- `forwards`
- `none`: 
- `backwards`
- `both`

It's kinda confusing tbh. Look at the docs.

There's another property called `animation-direction`, which ointeracts with `animation-fill-mode`, so keep an eye out for that.



