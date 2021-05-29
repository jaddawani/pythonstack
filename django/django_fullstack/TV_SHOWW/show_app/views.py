from django.shortcuts import render , redirect
from . import models
from django.contrib import messages

def show_all(request):
    return redirect('/show')
    


def show_tabel(request):

    context = {
        "tv_show" : models.all_tv()
    }

    return render(request,"show_tabel.html" , context)

def New_add_show(request):
    return render(request,"new_add_show.html")

def single_show(request):
    errors = models.TV.objects.basic_validator(request.POST)
        
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/show/new")
    else:
        
        
        if request.method == "POST":
            title = request.POST['title']
            network = request.POST['network']
            release_date= request.POST['release_date']
            description = request.POST['description']

            models.single_show(title , network , description , release_date)
            id = models.TV.objects.last().id

        return redirect("/show/"+str(id))
    

    


def show_details(request, id):

    context = {
        "shows" : models.TV.objects.get(id= id)
    }

    return render(request , "show_details.html", context)
 


def edit_show(request , id):


    context = {
        "x": models.TV.objects.get(id=id)
    }
   
    
    return render(request , "edit_show.html" , context)
    

def update_show(request , id):
    x=models.TV.objects.get(id=id)

    errors = models.TV.objects.basic_validator(request.POST)
        
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/show/edit/"+str(id))
    else:
        

        if request.method == "POST":
            x.title = request.POST['title']
            x.network = request.POST['network']
            x.release_date= request.POST['release_date']
            x.description = request.POST['description']

            x.save()

        return redirect("/show/"+ str(id))


def delete_show(request , id):

    x= models.TV.objects.get(id=id)
    x.delete()
    

    return redirect ('/show')




