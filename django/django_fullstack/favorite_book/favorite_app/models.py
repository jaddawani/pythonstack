from django.contrib import messages
from django.db import models


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["fname"] = "first name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "last name should be at least 2 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "your password should be at least 8 characters"
        return errors

    def book_validator(self , postdata):
        errors = {}

        if len(postdata['description']) < 2:
            errors["description"] = "description should be at least 2 characters"

        if len(postdata['title']) < 2:
            errors["title"] = "title should be at least 2 characters"


        return errors

class User(models.Model) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    Email= models.CharField(max_length=200)
    passwd = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploded_by =models.ForeignKey(User,related_name="books_uploded",on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User,related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()
    

def create_user(first_name , last_name , Email , passwd) : 
    
    
    return User.objects.create(first_name = first_name , last_name = last_name , Email = Email , passwd = passwd)


def get_user(Email):
    
    users=  User.objects.filter(Email=Email )
    if len(users)>0:
        return users[0]
    else:
        return None

    

def check_password(passwd, conpasswd):
  

    if passwd == conpasswd :


        return True


def add_book(title ,description  ,  id):
    
    

    created_book= Book.objects.create(title= title ,description= description, uploded_by= User.objects.get(id=id) )
    this_user= User.objects.get(id=id)
    created_book.users_who_like.add(this_user)
    return created_book


def all_books():
    print("models")

    return Book.objects.all()

def all_users():
    return User.objects.all()

def show_books(id):
    
    return Book.objects.get(id=id) 

def show_books2(id):
    this_user = User.objects.get(id=id)
    return this_user

def favorite(user_id , book_id):
    this_user = User.objects.get(id=user_id)
    this_book = Book.objects.get(id=book_id)
 
    return this_book.users_who_like.add(this_user)

def unfavorite(user_id , book_id):
    this_user = User.objects.get(id=user_id)
    this_book = Book.objects.get(id=book_id)
 
    return this_book.users_who_like.remove(this_user)


    


