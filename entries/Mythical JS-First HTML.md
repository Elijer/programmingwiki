# Mythical JS-First HTML
Literally lost some sleep on this last night. That's not to mention the hours I vaguely tried to implement it myself.

I think the seeds for this idea were planted when I tried out React for the first time. Writing JSX files, my mind was, like many, blown by being able to write HTML inside of my JS.

When I write very vanilla JS/HTML/CSS sites, I find myself wishing I could do this. I find myself wishing, actually, something quite specific:

I want write a `main.html` that loads a bundled `main.js` file, and that file then can call upon `html` or `js` files saved inside of some multi-level `template` folder. The templates can be pure HTML *or* they can be functions that take arguments and return HTML.

Javascripts ability to manipulate HTML is so extensive that I sort of can't believe that we aren't just writing our HTML in Javascript itself and possibly dropping the HTML file exension for the most part.

You can even do this of course, and plenty of people do. They just stop short, usually, of writing their entire HTML files inside of JS files. And probably rightly so. All those Divs and stuff, it can be nice to write out a whole view in it's own HTML only file and then manipulate it later.

But after that, much of content can end up being entirely dynamic. One page apps especially necessitate this. Any sort of complex webapps involve this principle.

So i guess all I really need is a way to get my HTML syntax to have syntax highlighting tbh. After that I think we're good? Then i can start on my dream of writing all my `html` in my `js` files, where it's going to get manipulated anyways, often just after being rendered anyways.