# Importing SCSS from another file
One of my favorite parts of SCSS is that it allows you to really easily break up your CSS into components or sections while still having only a single CSS entry point. When using a JS bundler, I think this mirrors the way JS can be broken down into ES6 modules in a really beautiful way. Plust it's pretty effin easy, just use:

```scss
@import "../../_variables";
```
