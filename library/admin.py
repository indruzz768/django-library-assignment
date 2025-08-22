from django.contrib import admin
from .models import Library, BookShelf, Book
# Register your models here.

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'pincode', 'contact_info']
    search_fields = ['name', 'location']

@admin.register(BookShelf)
class BookShelfAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'library']
    search_fields = ['name']
    list_filter = ['library']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'publisher', 'shelf']
    search_fields = ['name', 'author', 'publisher']
    list_filter = ['shelf']