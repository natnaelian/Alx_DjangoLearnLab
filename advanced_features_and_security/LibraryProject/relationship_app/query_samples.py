from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"No author found with name {author_name}"

def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"

def query_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to {library_name}"

# Example usage
if __name__ == "__main__":
    print("Books by Author 'Jane Doe':", query_books_by_author("Jane Doe"))
    print("Books in Library 'City Library':", query_books_in_library("City Library"))
    print("Librarian for Library 'City Library':", query_librarian_for_library("City Library"))