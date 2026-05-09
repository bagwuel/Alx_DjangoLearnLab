author = Author.objects.get(name='Emmanuel')
books = author.book_set.all()

library = Library.objects.get(name='mylibrary')
books = library.book.all()

library = Library.objects.get(name='mylibrary')
librarian = library.librarian_set
