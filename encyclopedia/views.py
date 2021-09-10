from numpy import random

from django.core.files.storage import FileSystemStorage
from markdown2 import Markdown
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from django.shortcuts import render

from django import forms

from encyclopedia.models import Entry

from . import util

class NewSearchForm(forms.Form):
    search = forms.CharField(label="New Search", min_length=0)
    # min_length=2, max_length=50, blank=False, null=False
    # priority = forms.IntegerField(label="Priority", min_value = 1, max_value = 5)

class NewEntryForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput
        (attrs={'class':'new_title', 'placeholder':'Title'}))
    content = forms.CharField(label="", widget=forms.Textarea
        (attrs={"class": "new-entry-content", 'placeholder':'Content'}))

def index(request):

    # Takes files and changes them into DB rows
    entries = util.list_entries()
    for entry in entries:
        content = util.get_entry(entry)
        util.save_to_db(entry, content)

    # Takes DB rows and turns them into entries
    files = Entry.objects.all()
    for file in files:
        util.save_entry(file.title, file.content)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewSearchForm()
    })

def entry(request, entry):
    content = util.get_entry(entry)
    if content:
        converted_content = convertToMarkdown(content)
        return render(request, "encyclopedia/entry.html", {
            "content": converted_content,
            "title": entry.capitalize(),
            "form": NewSearchForm()
        })
    else:
        return render(request, "encyclopedia/noResults.html", {
            "term": entry,
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
                    # return redirect(reverse("wiki:entry", args = [title]))
                    return redirect(reverse("wiki:alreadyExists", args = [title]))
                else:
                    util.save_entry(title, content)
                    # theFile = default_storage.save(f'./entries/{title}.md', ContentFile(f"# {title} \n" + content));
                    return redirect(reverse("wiki:entry", args = [title]))
        else:
            return HttpResponse("Not a valid http response for createPage method")

def alreadyExists(request, entry):
    return render(request, "encyclopedia/alreadyExists.html", {
        "title": entry
    })

def editPage(request, entry):
    content = util.get_entry(entry)
    # converted_content = convertToMarkdown(content)
    return render(request, "encyclopedia/edit.html", {
        "title": entry.capitalize(),
        "content": content
    })

def changeEntry(request):
    if request.method == "POST":
        content = request.POST["content"]
        title = request.POST["title"]

        util.save_entry(title, content)

        # util.save_to_db(title, content)

        # filePath = f'./entries/{title}.md'
        # default_storage.delete(filePath)
        # default_storage.save(filePath, ContentFile(content))
        return redirect(reverse("wiki:entry", args = [title]))

        # return HttpResponse(content)
    else:
        return HttpResponse("couldn't change form")

def randomEntry(request):
    allEntries = util.list_entries()
    leng = len(allEntries)
    randomNum = random.randint(leng)
    randEntryName = allEntries[randomNum]
    return redirect(reverse("wiki:entry", args = [randEntryName]))

def convertToMarkdown(content):
    markdowner = Markdown()
    converted_content = markdowner.convert(content)
    return converted_content