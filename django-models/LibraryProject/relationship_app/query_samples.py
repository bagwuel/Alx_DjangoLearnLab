author_name = 'Emmanuel'
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)


library_name = "mylibrary"
library = Library.objects.get(name=library_name)
books = library.book
all_books = books.all()

librarian = Librarian.objects.get(library=library)
