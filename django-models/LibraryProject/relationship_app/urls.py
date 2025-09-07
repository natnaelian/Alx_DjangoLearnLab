from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Function-based view
    path("books/", list_books, name="list_books"),

    # Class-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Secured book operations
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),

    # User registration
    path("register/", views.register_view, name="register"),

    # User login
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),

    # User logout
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
