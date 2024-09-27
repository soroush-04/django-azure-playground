from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .forms import BookForm
from .models import Book
from django.db.models import Q


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


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")  # redirect to the book list page
        else:
            print(form.errors)

    else:
        form = BookForm()
    return render(request, "add_book.html", {"form": form})


def book_list(request):
    query = request.GET.get("q")
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(published_date__icontains=query)
        )
    else:
        books = Book.objects.all()

    return render(request, "book_list.html", {"books": books})


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "edit_book.html", {"form": form})


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "confirm_delete.html", {"book": book})
