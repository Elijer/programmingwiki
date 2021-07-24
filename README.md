# Django

### URLs
I've had a lot of issues with the URL syntax, whether it's any of the following categories:
1. URL patterns specified in urls.py files
2. URL permalink thinks with the `{% url "app:path" variable %} syntax
3. {{ variable }} as something that could feasibly be used instead of #2 to generatively create URLs, maybe? Except I think Django heavily advises against this

To demystify these things, here are the docs for Django's URL syntax:
1. [URL dispatcher](https://docs.djangoproject.com/en/3.2/topics/http/urls/)

It has all that stuff in it.

### Questions
If a layout template that other pages use requires say, a form as a variable, do I need to then pass that in to every single page that uses that template? I don't know how else it would get the data. However, I tried omitting it, and the form still seemed to work. So the answer may be yes, but I can't explain why.

### Pain Points
1. This sucked:
`django decoding to str: need a bytes-like object, NoneType found`
It was caused by one URL pattern getting in the way of another, because it was sort of at the root URL of the app. there was `<str:entry>` and then there was just `search`. I don't know why I didn't realize they would conflict directly, and `search` would be read as IF IT WERE an article. So the solution was adding `wiki/<str:entry>`. That wiki subroute is useful obviously -- anything after wiki will be treated like a potential article, fine. Anything with search will be treated like a search. Then, when generatively listing the `href` attribute of my links on my index page, I used this: `"{% url 'pages:entry' entry %}"`, which apparently leads to the url of `root/pages/{{whatever the entry is}}`. So that `entry` variable at the end of the weird `{% url %}` thing is sort of treated like just a wildcard variable that gets plugged in to the end of that path. I wonder what happens if there are multiple wildcards to be placed after each other?