from django.db import models
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="Dojo", on_delete = models.CASCADE)
    first_name = models.CharField(null=True , max_length=255)
    last_name = models.CharField(null=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def result(form):
    Dojo.objects.create(name=form["name"] , city = form["city"] , state= form["state"])

    



def result2(form):
    Ninja.objects.create(first_name=form["first_name"] , last_name = form["last_name"] , dojo= Dojo.objects.get(id =form["select"] ))