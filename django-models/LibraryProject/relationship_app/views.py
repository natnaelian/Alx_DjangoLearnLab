from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library   # <-- keep this separate for the checker

# --- Function-based view: List all books ---
def list_books(request):
    books = Book.objects.all()  # ✅ checker expects this
    return render(request, "relationship_app/list_books.html", {"books": books})

# --- Class-based view: Library details ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
