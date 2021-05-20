
from django.shortcuts import redirect, render 
import random

from django.shortcuts import render

def index(request):
    
    request.session['random'] = random.randint(1, 100)
    print(request.session['random'])



    return render(request,'index.html' )

 	               
def index2(request):
    
    
    number = int(request.POST['guess'])

    if int(request.session['random']) >  number :
        num1= 1
    elif int(request.session['random']) < number :
        num1= 2
    else:
        num1= 3

    
    dict= {
    'number' : request.POST['guess'] ,
    'rand'  :request.session['random'],
    "num1" : num1

    }
    
    
    

    return render(request,'index2.html' , dict)

 	               




