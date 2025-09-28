from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# View for listing all books and creating new ones
class BookListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """
    Handles GET requests to list all books and POST requests to create a new book.
    Supports:
    - Filtering by title, author, publication_year (e.g., ?title=Book&author=1&publication_year=2023).
    - Searching by title and author name (e.g., ?search=Rowling).
    - Ordering by title, publication_year (e.g., ?ordering=-publication_year).
    Permissions: Read-only for unauthenticated users, full access for authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ]
    filterset_fields = ['title', 'author', 'publication_year']  # Fields for exact filtering
    search_fields = ['title', 'author__name']  # Fields for text-based search
    ordering_fields = ['title', 'publication_year']  # Fields for ordering
    ordering = ['title']  # Default ordering

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
        Customizes queryset to support filtering by author_id query parameter (backward compatibility).
        """
        queryset = super().get_queryset()
        author_id = self.request.query_params.get('author_id')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        return queryset

# View for retrieving, updating, or deleting a specific book
class BookDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    """
    Handles GET, PUT, and DELETE requests for a specific book identified by its primary key.
    Permissions: Read-only for unauthenticated users, full access for authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# View for creating a book via POST
class BookCreateView(generics.GenericAPIView):
    """
    Handles POST requests to create a new book at /api/books/create/.
    Expects book data (title, publication_year, author) in the request body.
    Permissions: Authenticated users only.
    """
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# View for updating a book via POST with ID in request body
class BookUpdateView(generics.GenericAPIView):
    """
    Handles POST requests to update a book. Expects 'id' and book data in the request body.
    Permissions: Authenticated users only.
    """
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        book_id = request.data.get('id')
        if not book_id:
            return Response({"error": "Book ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

# View for deleting a book via POST with ID in request body
class BookDeleteView(generics.GenericAPIView):
    """
    Handles POST requests to delete a book. Expects 'id' in the request body.
    Permissions: Authenticated users only.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        book_id = request.data.get('id')
        if not book_id:
            return Response({"error": "Book ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            book = Book.objects.get(pk=book_id)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)