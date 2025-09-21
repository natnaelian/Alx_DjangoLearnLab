# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# Create router and register BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Original ListAPIView (only GET all)
    path('books/', BookList.as_view(), name='book-list'),

    # Token retrieval endpoint
    path('auth-token/', obtain_auth_token, name='api_token_auth'),  

    # All CRUD operations via ViewSet
    path('', include(router.urls)),
]
