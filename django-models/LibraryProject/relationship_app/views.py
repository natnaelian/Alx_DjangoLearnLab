from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from .models import Book, Library


# -------------------------
# Function-based view: List all books
# -------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# -------------------------
# Class-based view: Library detail with all books
# -------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# -------------------------
# User Registration View
# -------------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            messages.success(request, "Registration successful!")
            return redirect("list_books")  # redirect to your book list
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# -------------------------
# User Login View
# -------------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("list_books")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# -------------------------
# User Logout View
# -------------------------
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request, "relationship_app/logout.html")
