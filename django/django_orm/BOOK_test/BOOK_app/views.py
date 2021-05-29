

from typing import ContextManager
from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from . import models
import BOOK_app


def book(request):
    Context = {

        "books": models.allbooks()

    }
    return render(request , "index.html" , Context)

def addbook(request):
    if request.method=='POST':
        title= request.POST['title']
        description =request.POST['description']

        models.addbook(title,description)

    return redirect('/') 


def showbook(request, id):



    context = {
        'this_book':models.getbook(id),
        "all_authors" : models.allAuthors()
    }

    return render(request,"welcome.html" , context)

def AuthorToBook(request):
    if request.method =='POST':
        selected_author = request.POST['selected_author']
        book_id = request.POST['book_id']
        models.AuthorToBook(selected_author,book_id )

    return redirect('/shows/'+str(book_id))

