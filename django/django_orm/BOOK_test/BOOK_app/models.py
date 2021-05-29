from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255 , default="jad")
    last_name = models.CharField(max_length=255 , default="dawani")
    books = models.ManyToManyField(Book, related_name="Authors")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def addbook(title , description):
    new_book= Book.objects.create(title=title , description=description)
    return new_book

def allbooks():
   return Book.objects.all()

def getbook(id):
    return  Book.objects.get(id=id)


def allAuthors():
   return Author.objects.all()

def AuthorToBook(author_id , book_id):
   this_book= Book.objects.get(id=book_id)
   this_author = Author.objects.get(id=author_id)
   this_book.Authors.add(this_author)
    






