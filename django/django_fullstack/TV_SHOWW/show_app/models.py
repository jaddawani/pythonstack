from django.db import models

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors["title"] = "Blog name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Blog description should be at least 3 characters"
        if len(postData['description']) < 3:
            errors["description"] = "Blog description should be at least 3 characters"
        return errors


class TV(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    description=models.TextField()
    release_date= models.DateField(default="2020-1-1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()


def all_tv():
    shows=TV.objects.all()
    return shows


def single_show(title , network , description , release_date):
    TV.objects.create(title= title , network=network , release_date = release_date , description=description)

def edit_show(id):
    x= TV.objects.get(id=id)
    return x
