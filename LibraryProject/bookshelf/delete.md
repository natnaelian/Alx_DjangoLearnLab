from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.delete()
# Output: (1, {'bookshelf.Book': 1})

# Confirm deletion
print(Book.objects.all())
#