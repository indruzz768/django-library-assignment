from rest_framework import serializers
from .models import Library, BookShelf, Book

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

    def validate_name(self, value):
        if Library.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("A library with this name already exists.")
        return value

class BookShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookShelf
        fields = '__all__'

    def validate(self, data):
        library = data.get('library')
        name = data.get('name')

        if not Library.objects.filter(id=library.id).exists():
            raise serializers.ValidationError("Linked library does not exist.")

        # Check if same shelf name exists within the same library
        if BookShelf.objects.filter(name__iexact=name, library=library).exists():
            raise serializers.ValidationError("Shelf with this name already exists in this library.")

        return data

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        name = data.get('name')
        author = data.get('author')
        publisher = data.get('publisher')
        shelf = data.get('shelf')

        if not BookShelf.objects.filter(id=shelf.id).exists():
            raise serializers.ValidationError("Linked shelf does not exist.")

        if Book.objects.filter(
            name__iexact=name,
            author__iexact=author,
            publisher__iexact=publisher
        ).exists():
            raise serializers.ValidationError("A book with the same name, author, and publisher already exists.")

        return data
