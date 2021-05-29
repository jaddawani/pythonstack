from django.db import models

class Book(models.Model):
    description = models.CharField(max_length=255 , default=200)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="publishers")
    notes = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


