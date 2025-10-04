from django.db import models

# Author model to store information about authors
class Author(models.Model):
    name = models.CharField(max_length=100)  # Stores the author's name, max length of 100 characters

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Orders authors alphabetically by name

# Book model to store information about books
class Book(models.Model):
    title = models.CharField(max_length=200)  # Stores the book’s title, max length of 200 characters
    publication_year = models.IntegerField()  # Stores the year the book was published
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,  # Deletes books if the associated author is deleted
        related_name='books'  # Allows reverse lookup from Author to Books (e.g., author.books)
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']  # Orders books alphabetically by title

