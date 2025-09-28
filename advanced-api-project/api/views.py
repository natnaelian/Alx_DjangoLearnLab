from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


# ===============================
# BOOK LIST VIEW
# ===============================
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Retrieves a list of all books with support for:
    - Filtering by title, author name, and publication_year
    - Searching by title and author name
    - Ordering by title or publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search fields (text search)
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


# ===============================
# BOOK DETAIL VIEW
# ===============================
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
    Retrieves a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ===============================
# BOOK CREATE VIEW
# ===============================
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Allows authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ===============================
# BOOK UPDATE VIEW
# ===============================
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /api/books/<id>/update/
    PATCH /api/books/<id>/update/
    Allows authenticated users to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ===============================
# BOOK DELETE VIEW
# ===============================
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<id>/delete/
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
