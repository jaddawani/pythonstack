
from django.shortcuts import redirect, render

from django.shortcuts import render, HttpResponse 

def countt(request):
    if 'number' in request.session:
        request.session['number']+=1
    else: request.session['number']=0

    return render(request,'index.html')


def clears(request):
    request.session.clear
    request.session['number']=0
    return redirect('/') 

