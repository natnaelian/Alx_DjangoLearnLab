from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# === LIST VIEW ===
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Retrieves a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# === DETAIL VIEW ===
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Retrieves a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# === CREATE VIEW ===
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Allows authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# === UPDATE VIEW ===
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /books/<id>/update/
    Allows authenticated users to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# === DELETE VIEW ===
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/delete/
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
