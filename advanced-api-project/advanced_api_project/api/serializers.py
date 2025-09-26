from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model:
    - Serializes all fields of the Book model.
    - Includes validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation:
        Ensure that the publication year is not in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model:
    - Serializes the author’s name.
    - Uses nested BookSerializer to include related books.
    """
    books = BookSerializer(many=True, read_only=True)  
    # 'books' matches the related_name in the Book model.

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
