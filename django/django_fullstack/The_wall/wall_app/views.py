from django.http import request
from django.shortcuts import render
from django.shortcuts import render, redirect 
from . import models
from django.contrib import messages
import bcrypt



def index(request):

    return render(request,"index.html")

def main_wall(request):

    context = {
       "all_messages": models.all_messages,
       "all_comments" : models.all_comments

    }

       
    return render(request,"main_wall.html",context)


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
                return redirect('/main_wall')
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
            return redirect('/main_wall')
    return redirect('/')



def add_message(request):
    if request.method == "POST":
        create_message=request.POST['message']
        user_id=request.session['id']
        print("views")
    models.add_message(create_message , user_id)

    return redirect("/main_wall")


def add_comment(request):
    if request.method == "POST":
        create_comment = request.POST['comment']
        user_id = request.session['id']
        message_id = request.POST['message']

    models.add_comment(create_comment , user_id , message_id)

    return redirect("/main_wall")





    
