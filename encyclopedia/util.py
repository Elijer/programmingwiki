import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from encyclopedia.models import Entry


def list_entries():

    # Returns a list of all names of encyclopedia entries.

    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

def refresh_DB():
    entries = list_entries()
    for entry in entries:
        content = util.get_entry(entry)
        save_to_db(entry, content)

def search_entries(bigList, substring):
    bigList = list_entries()
    newList = []
    for item in bigList:
        item = item.lower()
        substring = substring.lower()
        if substring in item:
            newList.append(item)
    return newList

def save_to_db(title, content):
    if Entry.objects.filter(ref=title.lower()).exists():
        e = Entry.objects.get(ref=title.lower())
        e.content = content
        e.save()
    else:
        e = Entry(
            ref = title.lower(),
            title = title,
            content = content
        )
    e.save();

def save_entry(title, content):
    # Saves an encyclopedia entry, given its title and Markdown
    # content. If an existing entry with the same title already exists,
    # it is replaced.

    # Save to SQL db
    save_to_db(title, content)

    # Save file to directory
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    # A lot of this will be repeated from save_to_db() and could be consolidated into a single function
    ref = title.lower()
    if Entry.objects.filter(ref=title.lower()).exists():
        e = Entry.objects.get(ref=ref)
        capsTitle = e.title # this is the capsensitive version, while entry.ref is always lowercase
        f = default_storage.open(f"entries/{capsTitle}.md")
        return f.read().decode("utf-8")
    else:
        return None
