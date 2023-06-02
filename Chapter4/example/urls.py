from django.urls import path, include
from .views import HelloAPI
from .views import bookAPI
from .views import booksAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
]