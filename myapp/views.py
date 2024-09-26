from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .forms import BookForm


def home(request):
    return render(request, "home.html")


def hello_world(request):
    return HttpResponse("Hello, World!")


@csrf_exempt
def greeting(request):
    if request.method == "POST":
        name = request.POST.get("name", "World")
        return HttpResponse(f"Hello, {name}!")
    return HttpResponse("Send a POST request to get a greeting.")


# @csrf_exempt
# class GreetingView(View):
#     def get(self, request):
#         return HttpResponse("This is a class-based view.")

#     def post(self, request):
#         name = request.POST.get("name", "World")
#         return HttpResponse(f"Hello, {name} from a class-based view!")


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")  # redirect to the book list page

    else:
        form = BookForm()
    return render(request, "myapp/add_book.html", {"form": form})
