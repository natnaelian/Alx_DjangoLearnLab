from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from django_filters import rest_framework as filters_backend   # 👈 this matches your requirement
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
    permission_classes = [AllowAny]

    # Enable filtering, searching, ordering
    filter_backends = [filters_backend.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


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
    permission_classes = [AllowAny]


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
    permission_classes = [IsAuthenticated]


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
    permission_classes = [IsAuthenticated]


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
    permission_classes = [IsAuthenticated]
