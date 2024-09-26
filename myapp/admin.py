from django.contrib import admin

# Register your models here.

from .models import Book
from .forms import BookForm

# admin.site.register(Book)


class BookAdmin(admin.ModelAdmin):
    form = BookForm


admin.site.register(Book, BookAdmin)
