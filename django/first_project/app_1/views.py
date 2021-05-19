
from django.http import request
from django.shortcuts import redirect, render , HttpResponse
from django.http import JsonResponse


def root(request):

    return redirect("/blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog") 

def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}") 


def edit(request,number):
    return HttpResponse("placeholder to edit blog {number}")

def destroy(request,number):
    return redirect ("/blogs")


def json(request):
        return JsonResponse({"title": "JSON", "content": "Anything goes here"})

def index(request):
    return render(request, "index.html")

    # return HttpResponse("placeholder to later display a list of all blogs")

def create(request):
    return redirect("/")



