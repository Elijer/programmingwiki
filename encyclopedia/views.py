from markdown2 import Markdown

from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdowner = Markdown()
    content = util.get_entry(entry)
    converted_content = markdowner.convert(content)
    return render(request, "encyclopedia/entry.html", {
        "content": converted_content,
        "title": entry.capitalize()
    })