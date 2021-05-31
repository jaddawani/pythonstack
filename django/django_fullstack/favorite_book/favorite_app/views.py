from django.http import request
from django.shortcuts import render
from django.shortcuts import render, redirect 
from . import models
from django.contrib import messages
import bcrypt




def index(request):

    return render(request,"index.html")

def favorite(request):
    context = {
        "all_books" : models.all_books,
        "user" : models.all_users
    }
        
    return render(request,"favorite.html" ,context)


def logout(request):
    request.session.clear()
    return redirect('/')
    

 

def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    

    if len(errors) > 0:
       
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
    else:
        print('start reg')
        if request.method == "POST" :
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            Email = request.POST['Email']
            passwd = request.POST['passwd']
            conpasswd = request.POST['conpasswd']
            

            if models.check_password(passwd, conpasswd)  :
                hashed_passwd = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()
                print('passwords are confirmed')
                user = models.create_user(first_name ,last_name , Email , hashed_passwd)
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name 
                return redirect('/favorite')
    return redirect('/')



def login(request) :
    if request.method == "POST":
        Email = request.POST['Email']
        passwd = request.POST['passwd']
        user= models.get_user(Email)
        
        
        if user and bcrypt.checkpw(passwd.encode(), user.passwd.encode()):
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name 
            return redirect('/favorite')
    return redirect('/')

def add_book(request):

    errors = models.Book.objects.book_validator(request.POST)
        
    if len(errors):
        
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/book"+str(id))
    else:
        
        if request.method == "POST":
            title=request.POST['title']
            description=request.POST['description']
            user_id = request.session['id']
        

            x = models.add_book (title, description ,  user_id)
            # x.id = the book id we created up

            models.favorite(user_id , x.id)

            return redirect ("/favorite")

        return redirect("/favorite")
    

def show_book(request,id ):
    selected_book=models.show_books(id=id)
    context = {
        "book" : models.show_books(id=id),
       
    }
    print(selected_book.users_who_like.all())
    return render(request,"show_book.html" , context)

def show_books2(request , id):

    context = {
        "user3" : models.show_books2(id)
    }

    return render (request , "show_book.html" , context)



def delete_show(request , id):

    x= models.Book.objects.get(id=id)
    x.delete()
    

    return redirect ('/favorite')


def update_show(request , id):
    x=models.Book.objects.get(id=id)

    errors = models.Book.objects.book_validator(request.POST)
        
    if len(errors)>0:
        
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/book/"+str(id))
    else:
        

        if request.method == "POST":
            x.title = request.POST['title']
            
            x.description = request.POST['description']

            x.save()

        return redirect("/book/"+ str(id))


def add_fav(request , id):
    if "id" in request.session:
        models.favorite(request.session['id'], id)
        return redirect("/favorite")

def remove_fav(request,id):
    if "id" in request.session:
        models.unfavorite(request.session['id'], id)
        return redirect("/favorite")




