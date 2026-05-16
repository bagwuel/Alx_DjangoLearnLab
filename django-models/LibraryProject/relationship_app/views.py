from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book
# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):

    return render(request, "relationship_app/profile.html")

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "relationship_app/register.html"
    success_url = reverse_lazy("login")

def books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {books:books})

class LibraryDetails(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
