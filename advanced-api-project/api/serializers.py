from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']  # Serialize all fields of the Book model

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication year is not in the future.
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author model with nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer to include related books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Include author's name and related books

    """
    The 'books' field uses the BookSerializer to dynamically serialize all books related to an author
    through the ForeignKey relationship (author.books). The 'many=True' argument indicates that
    multiple Book instances can be serialized. The 'read_only=True' ensures that books are only
    retrieved and not modified through this serializer.
    """