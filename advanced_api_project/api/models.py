from django.db import models

class Author(models.Model):
    """
    Author model:
    Represents a book author.
    - name: Stores the author’s name.
    One author can have many books (one-to-many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    Represents a book written by an author.
    - title: Title of the book.
    - publication_year: Year the book was published.
    - author: ForeignKey relationship to Author (one-to-many).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
