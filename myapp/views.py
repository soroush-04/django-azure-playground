from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def hello_world(request):
    return HttpResponse("Hello, World!")
