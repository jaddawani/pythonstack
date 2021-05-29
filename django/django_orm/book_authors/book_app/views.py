from django.shortcuts import redirect, render , HttpResponse
from . import  models
from .models import Book




def index(request):
    context = {
    	"all_the_books": models.Book.objects.all()
    }
    return render(request, "index.html", context)



def index2(request):
    Book.objects.create(title= request.POST["title"], description = request.POST["description"])
    return redirect("/")

def index3(request, x):
    x= Book.objects.get(id=x)
    context = {
    	"x": x
    }

    return render(request, "book2.html" ,context)


