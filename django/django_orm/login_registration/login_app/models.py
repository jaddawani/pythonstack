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
    # cars = a list of cars assioated with a given user

class car(models.Model):
    name = models.CharField(max_length=200)
    model =  models.IntegerField()
    clients = models.ManyToManyField(User , related_name="cars" )
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

    


def get_user_cars(id):
    user = User.objects.get(id=id)
    return user.cars.all()

def check_password(passwd, conpasswd):
    # ok = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()
    # okay = bcrypt.hashpw(conpasswd.encode(), bcrypt.gensalt()).decode()

    if passwd == conpasswd :

        return True