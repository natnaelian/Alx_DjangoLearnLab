from django.contrib import admin
from .models import Author, Book

# Register Author model with admin interface
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']  # Display name in admin list view
    search_fields = ['name']  # Enable search by name

# Register Book model with admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_year', 'author']  # Display key fields in admin list view
    list_filter = ['author']  # Allow filtering by author
    search_fields = ['title']  # Enable search by title