from myapp.models import Book
from myapp.serializers import BookSerializer

def run():
    # Create a sample book
    book = Book(title="Sample Book", author="John Doe", published_date=2023, isbn="1234567890123")
    book.save()

    # Serialize the book
    serializer = BookSerializer(book)
    print(serializer.data)
