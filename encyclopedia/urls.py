from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("pages/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new", views.newPage, name="new"),
    path("create", views.createPage, name="create"),
    path("edit/<str:entry>", views.editPage, name="edit"),
    path("change", views.changeEntry, name="change")
]