# myapp/urls.py

from django.urls import path
from . import views

# from .views import GreetingView

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/", views.hello_world, name="hello"),
    path("greeting/", views.greeting, name="greeting"),
    path("add_book/", views.add_book, name="add_book"),
    path("books/", views.book_list, name="book_list"),
]
