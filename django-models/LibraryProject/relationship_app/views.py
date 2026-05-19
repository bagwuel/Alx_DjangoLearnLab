from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book
# Create your views here.
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.is_authenticated and user.userprofile.role == "Admin"


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == "Librarian"


def is_member(user):
    return user.is_authenticated and user.userprofile.role == "Member"



@login_required
def profile(request):

    return render(request, "relationship_app/profile.html")
'''
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "relationship_app/register.html"
    success_url = reverse_lazy("login")
'''

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:
        form = UserCreationForm()

    return render(
        request,
        "relationship_app/register.html",
        {
            "form": form
        }
    )


def books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {books:books})

class LibraryDetails(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
        return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
