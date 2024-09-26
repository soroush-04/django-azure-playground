from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")


def hello_world(request):
    return HttpResponse("Hello, World!")


@csrf_exempt
def greeting(request):
    print("Request Method:", request.method)
    if request.method == "POST":
        name = request.POST.get("name", "World")
        print("Name received:", name)
        return HttpResponse(f"Hello, {name}!")
    return HttpResponse("Send a POST request to get a greeting.")
