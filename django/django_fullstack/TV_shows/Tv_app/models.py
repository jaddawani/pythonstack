from django.db import models
from django.http import request

class TV(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date= models.DateField(default="2020-1-1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def all_tv():
    return TV.objects.all()

def special_tv(id):
    return TV.objects.get(id = id)

def set_tv(title, network, release_date):
    TV.objects.create(title=title , network=network , release_date=release_date)
    last_tv = TV.objects.last()
    return last_tv.id

    