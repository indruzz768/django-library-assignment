from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=255, unique=True)  # unique
    location = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    contact_info = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BookShelf(models.Model):
    library = models.ForeignKey(
        Library,
        related_name="shelves",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent duplicate shelf names inside same library
        unique_together = ("library", "name")

    def __str__(self):
        return f"{self.name} ({self.library.name})"


class Book(models.Model):
    shelf = models.ForeignKey(
        BookShelf,
        related_name="books",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent duplicate books with same name+author+publisher
        unique_together = ("name", "author", "publisher")

    def __str__(self):
        return f"{self.name} by {self.author}"
