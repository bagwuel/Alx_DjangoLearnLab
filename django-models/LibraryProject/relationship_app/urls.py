from django.urls import path
from . import views

urlpatterns = [
        path(
            "books/", views.books, name="books"
            ),
        path(
            "libraries/<int:pk>", views.LibraryDetails.as_view(), name="library_details"
            ),

]
