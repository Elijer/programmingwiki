# What is Redom for?

## Elements
`el`, an alias for html, is a helper for `document.createElement` with a couple differences. The main idea is simply to create elements with `el` and then mount them with `mount`.

## Mount
You can mount elements/components with `mount(parent, child, [before])`. If you define the third parameter, it works like `insertBefore` and otherwise it’s like `appendChild`.

Lastly, you can also replace elements by using the third argument `[appendChild` and then add a fourth argument `true`.

Mount will trigger the onmount lifecycle event the first time you mount a child. If you mount the same child again to the same parent, onremountgets called. If you mount it to another place, onunmount and onmount get called. Find more information on mounting here.

## Components
You can create components in Redom by defining a class, or function, which returns an object with at least an `el` property. (with something called `list` in redom, it should also return an `update` property.