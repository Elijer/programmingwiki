from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("pages/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search")
]