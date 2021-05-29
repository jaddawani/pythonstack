from django.shortcuts import redirect, render , HttpResponse
from . import models
from django.contrib import messages
import bcrypt





def index(request):

    return render(request,"index.html")

def welcome(request):
    if "id" in request.session:
        context ={
            'cars' : models.get_user_cars( request.session['id'])
        }
        return render(request,"welcome.html" , context)


    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")
    

 

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
                return redirect('/welcome')
    return redirect('/')



def login(request) :
    if request.method == "POST":
        Email = request.POST['Email']
        passwd = request.POST['passwd']
        user= models.get_user(Email)
        print(user)
        if user and bcrypt.checkpw(passwd.encode(), user.passwd.encode()):
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name 
            return redirect('/welcome')
    return redirect('/')




