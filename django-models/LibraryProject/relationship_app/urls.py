from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
        path(
            "books/", books, name="books"
            ),
        path(
            "libraries/<int:pk>", LibraryDetails.as_view(), name="library_details"
            ),

]
