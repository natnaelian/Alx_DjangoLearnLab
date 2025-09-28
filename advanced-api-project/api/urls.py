from django.urls import path
from .views import BookListView, BookDetailView, BookUpdateView, BookDeleteView

# URL patterns for the API app
app_name = 'api'

urlpatterns = [
    # Endpoint for listing all books and creating a new book
    path('books/', BookListView.as_view(), name='book-list'),
    # Endpoint for retrieving, updating, or deleting a specific book by ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    # Endpoint for updating a book via POST (requires 'id' in request body)
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    # Endpoint for deleting a book via POST (requires 'id' in request body)
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]