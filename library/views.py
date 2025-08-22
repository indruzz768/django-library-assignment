from django.shortcuts import render
from rest_framework import generics
from .models import Library, BookShelf, Book
from .serializers import LibrarySerializer, BookShelfSerializer, BookSerializer

class LibraryListCreateView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class LibraryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class BookShelfListCreateView(generics.ListCreateAPIView):
    queryset = BookShelf.objects.all()
    serializer_class = BookShelfSerializer

class BookShelfDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookShelf.objects.all()
    serializer_class = BookShelfSerializer

from rest_framework import filters

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author', 'publisher']

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



