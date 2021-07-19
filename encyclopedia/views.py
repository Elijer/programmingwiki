from markdown2 import Markdown
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from django.shortcuts import render

from django import forms

from . import util

class NewSearchForm(forms.Form):
    search = forms.CharField(label="New Search")
    # priority = forms.IntegerField(label="Priority", min_value = 1, max_value = 5)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewSearchForm()
    })

def entry(request, entry):
    content = util.get_entry(entry)
    converted_content = getMarkdownFile(content)
    return render(request, "encyclopedia/entry.html", {
        "content": converted_content,
        "title": entry.capitalize(),
        "form": NewSearchForm()
    })

def search(request):
    if request.method == "GET":
        searchField = request.GET['q']
        if searchField:
            content = util.get_entry(entry)
            if content:
                getMarkdownFile(searchField)


        
        return redirect(reverse("wiki:entry", args=[searchField]))

        # form = NewSearchForm(request.GET)
        #if form.is_valid():
            #searchField = form.cleaned_data["search"]

            # request.GET['q']
            # form['search'].value()
            # form.cleaned_data['q']

            
            # return redirect(reverse("wiki:entry", args=[searchField]))
    else:
        return HttpResponse("entry doesn't exist -- create page for this")

def getMarkdownFile(content):
    markdowner = Markdown()
    converted_content = markdowner.convert(content)
    return converted_content