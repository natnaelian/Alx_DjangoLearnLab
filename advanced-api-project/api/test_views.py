from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints
    - CRUD operations
    - Filtering, searching, ordering
    - Authentication & permission checks
    """

    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.other_user = User.objects.create_user(username="otheruser", password="otherpass")

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(title="Alpha Book", author=self.author1, publication_year=2001)
        self.book2 = Book.objects.create(title="Beta Book", author=self.author2, publication_year=1999)

        # API client
        self.client = APIClient()

    # ----------------------------
    # READ TESTS
    # ----------------------------
    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha Book")

    # ----------------------------
    # CREATE TESTS
    # ----------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse("book-create")
        data = {
            "title": "Gamma Book",
            "author": self.author1.id,
            "publication_year": 2010,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Gamma Book")

    def test_create_book_unauthenticated(self):
        url = reverse("book-create")
        data = {
            "title": "Unauthorized Book",
            "author": self.author1.id,
            "publication_year": 2020,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ----------------------------
    # UPDATE TESTS
    # ----------------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Alpha Book"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Alpha Book")

    def test_update_book_unauthenticated(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Should Fail"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ----------------------------
    # DELETE TESTS
    # ----------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse("book-delete", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_delete_book_unauthenticated(self):
        url = reverse("book-delete", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ----------------------------
    # FILTER / SEARCH / ORDER TESTS
    # ----------------------------
    def test_filter_books_by_author(self):
        url = reverse("book-list") + f"?author__name={self.author1.name}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Alpha Book")

    def test_search_books_by_title(self):
        url = reverse("book-list") + "?search=Beta"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Beta Book")

    def test_order_books_by_year(self):
        url = reverse("book-list") + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))
