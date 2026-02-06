
book = Book(title='1984', author='George Orwell', publication_year=1949)

book.save()

mybook = Book.objects.all()
mybook

<!-- <QuerySet [<Book: title: 1984, author: George Orwell, publication_year: 1949>]> -->

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

book = Book.objects.get(id=1)
book.delete()

