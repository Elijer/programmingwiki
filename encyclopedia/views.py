from django.core.files.storage import FileSystemStorage
from markdown2 import Markdown
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from django.shortcuts import render

from django import forms

from . import util

class NewSearchForm(forms.Form):
    search = forms.CharField(label="New Search")
    # priority = forms.IntegerField(label="Priority", min_value = 1, max_value = 5)

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Entry Title")
    content = forms.CharField(label="Entry Content", widget=forms.Textarea)

class NewEditForm(forms.Form):
    content = forms.CharField(label="Entry Content", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewSearchForm()
    })

def entry(request, entry):
    content = util.get_entry(entry)
    converted_content = convertToMarkdown(content)
    return render(request, "encyclopedia/entry.html", {
        "content": converted_content,
        "title": entry.capitalize(),
        "form": NewSearchForm()
    })

def search(request):
    if request.method == "GET":
        entry = request.GET['q']
        content = util.get_entry(entry)
        if content != None:
            return redirect(reverse("wiki:entry", args = [entry]))
        elif entry:
            bigList = util.list_entries()
            results = util.search_entries(bigList, entry)
            # return HttpResponse(results)
            if results:
                return render(request, "encyclopedia/search.html", {
                    "results": results,
                    "term": entry,
                    "form": NewSearchForm()
                    # Do I need to include NewSearchForm()?
                })
            else:
                return render(request, "encyclopedia/noResults.html", {
                    "term": entry,
                })

def newPage(request):
    return render(request, "encyclopedia/newPage.html", {
        "form": NewEntryForm()
    })

def createPage(request):
        if request.method == "POST":
            form = NewEntryForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]
                content = form.cleaned_data["content"]
                alreadyExists = util.get_entry(title)
                if alreadyExists:
                    return HttpResponse("page already exists")
                else:
                    theFile = default_storage.save(f'./entries/{title}.md', ContentFile(f"# {title} \n" + content));
                    return redirect(reverse("wiki:entry", args = [title]))
        else:
            return HttpResponse("Not a valid http response for createPage method")

def editPage(request, entry):
    content = util.get_entry(entry)
    # converted_content = convertToMarkdown(content)
    return render(request, "encyclopedia/edit.html", {
        "title": entry.capitalize(),
        "form": NewEditForm(),
        "content": content
    })

def convertToMarkdown(content):
    markdowner = Markdown()
    converted_content = markdowner.convert(content)
    return converted_content