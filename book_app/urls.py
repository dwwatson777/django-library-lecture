from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="book_list"),
    path("new", book_create, name="book_create"),
    path("<int:book_id>", book_view, name="book_detail"),
    path("<int:book_id>/update", book_update, name="book_update"),
    path("<int:book_id>/delete", book_delete, name="book_delete"),
]
