from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="book_list"),
    path("<int:book_id>", book_view, name="book_detail"),
    path("new", book_create, name="book_create")
]
