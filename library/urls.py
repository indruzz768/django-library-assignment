
from django.urls import path
from .views import (
    LibraryListCreateView,
    LibraryDetailView,
    BookShelfListCreateView,
    BookShelfDetailView,
    BookListCreateView,
    BookDetailView
)



urlpatterns = [
    
    path("libraries/", LibraryListCreateView.as_view(), name="library-list-create"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path("shelves/", BookShelfListCreateView.as_view(), name="shelf-list-create"),
    path("shelves/<int:pk>/", BookShelfDetailView.as_view(), name="shelf-detail"),
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
