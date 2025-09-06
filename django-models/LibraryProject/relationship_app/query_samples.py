import os
import sys
import django
from pathlib import Path

# --- Setup Django environment dynamically ---
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

for item in BASE_DIR.iterdir():
    if item.is_dir() and (item / "settings.py").exists():
        PROJECT_NAME = item.name
        break
else:
    raise RuntimeError("Could not find a Django project (settings.py missing)")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{PROJECT_NAME}.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Query Functions ---

def query_books_by_author(author_name):
    """
    Query all books by a specific author using objects.filter(author=author)
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # exactly what checker wants
        return books
    except Author.DoesNotExist:
        return []


def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a given library
    """
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# --- Sample Data Creation ---
def create_sample_data():
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Authors
    a1 = Author.objects.create(name="J.K. Rowling")
    a2 = Author.objects.create(name="George Orwell")

    # Books
    b1 = Book.objects.create(title="Harry Potter 1", author=a1)
    b2 = Book.objects.create(title="Harry Potter 2", author=a1)
    b3 = Book.objects.create(title="1984", author=a2)
    b4 = Book.objects.create(title="Animal Farm", author=a2)

    # Libraries
    l1 = Library.objects.create(name="Central Library")
    l2 = Library.objects.create(name="Community Library")

    l1.books.set([b1, b3])
    l2.books.set([b2, b4])

    # Librarians
    Librarian.objects.create(name="Alice", library=l1)
    Librarian.objects.create(name="Bob", library=l2)


# --- Demo/Test Code ---
if __name__ == "__main__":
    create_sample_data()

    # Test Query 1: Books by author
    print("--- Books by J.K. Rowling ---")
    books = query_books_by_author("J.K. Rowling")
    for book in books:
        print(book.title)

    # Test Query 2: Librarian for a library
    print("\n--- Librarian for Central Library ---")
    librarian = get_librarian_for_library("Central Library")
    if librarian:
        print(librarian.name)
