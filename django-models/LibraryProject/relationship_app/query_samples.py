author = Author.objects.get(name='Emmanuel')
books = author.book_set.all()


library_name = "mylibrary"
library = Library.objects.get(name=library_name)
books = library.book
all_books = books.all()

library = Library.objects.get(name='mylibrary')
librarian = library.librarian_set
