from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
        path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
        path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
        path('register/', views.register, name='register'),
        path('profile/', views.profile, name='profile'),
        path(
            "books/", views.books, name="books"
            ),
        path(
            "libraries/<int:pk>", views.LibraryDetails.as_view(), name="library_details"
            ),

]
