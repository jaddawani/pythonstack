

from typing import ContextManager
from django.http import request
from django.shortcuts import redirect, render

from . import models


def index(request):

    Context = {
        'all_dojo' : models.Dojo.objects.all().values(),
        "all_ninja" : models.Ninja.objects.all().values(),
        
    }

    

    return render(request , "index.html", Context)


def index2(request):
    if request.POST['forms'] == 'dojo' :
        models.result(request.POST)
    if request.POST['forms'] == 'ninja':
        models.result2(request.POST)

    return redirect('/')







