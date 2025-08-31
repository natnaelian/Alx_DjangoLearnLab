from django.contrib import admin
from .models import Book

# Register Book model with custom admin settings
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters to the right sidebar
    list_filter = ("publication_year", "author")

    # Enable search by title and author
    search_fields = ("title", "author")
