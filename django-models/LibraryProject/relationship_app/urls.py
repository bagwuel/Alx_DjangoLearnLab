from django.urls import path
from .views import books, LibraryDetails, RegisterView, profile

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
        path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
        path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
        path('register/', RegisterView.as_view(), name='register'),
        path('profile/', profile, name='profile'),
        path(
            "books/", books, name="books"
            ),
        path(
            "libraries/<int:pk>", LibraryDetails.as_view(), name="library_details"
            ),

]
