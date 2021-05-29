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

class User(models.Model) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    Email= models.CharField(max_length=200)
    passwd = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()



class Message(models.Model) :
    message_text = models.TextField(default= 'new message')
    user =models.ForeignKey(User,related_name="message_users",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model) :
    comment_text = models.TextField(default= 'new comment')
    user =models.ForeignKey(User,related_name="comment_users",on_delete=models.CASCADE)
    message =models.ForeignKey(Message,related_name="comment_messages",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    

    


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


def add_message(create_message , id):
    return Message.objects.create(message_text= create_message , user= User.objects.get(id=id))

def all_messages():
    print("models")

    return Message.objects.all()
   

def add_comment(create_comment , user_id , message_id):
    return Comment.objects.create(comment_text = create_comment , user= User.objects.get(id=user_id) , message=Message.objects.get(id=message_id) )

def all_comments():
    return Message.objects.all()




