import os
import sys
import django
from pathlib import Path

# --- Auto-detect settings module ---
# Get the base directory (where manage.py is located)
BASE_DIR = Path(__file__).resolve().parent.parent

# Add BASE_DIR to Python path
sys.path.append(str(BASE_DIR))

# Find the Django project folder (the one with settings.py inside)
for item in BASE_DIR.iterdir():
    if item.is_dir() and (item / "settings.py").exists():
        PROJECT_NAME = item.name
        break
else:
    raise RuntimeError("Could not find a Django project (settings.py missing)")

# Set environment variable dynamically
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{PROJECT_NAME}.settings")

# Setup Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Create Sample Data ---
def create_sample_data():
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")

    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)

    lib1 = Library.objects.create(name="Central Library")
    lib2 = Library.objects.create(name="Community Library")

    lib1.books.set([book1, book3])
    lib2.books.set([book2, book4])

    Librarian.objects.create(name="Alice", library=lib1)
    Librarian.objects.create(name="Bob", library=lib2)


# --- Queries ---
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")


def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")


def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian of {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")


# --- Demo calls ---
if __name__ == "__main__":
    create_sample_data()

    print("\n--- Query Samples ---")
    books_by_author("J.K. Rowling")
    books_in_library("Central Library")
    librarian_of_library("Central Library")
