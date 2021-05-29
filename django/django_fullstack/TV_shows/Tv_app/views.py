from django.shortcuts import redirect, render
from . import models

def index(request):

    return redirect("/shows")


def index2(request):
    context = {
        "TVs":models.all_tv()
    }
    return render(request,'index.html', context)

def show(request):

    return render(request, "index2.html")


def create_tv(request):
    if request.method == "POST":
        request.session['title'] = request.POST['title']
        request.session['network'] = request.POST['network']
        request.session['description']= request.POST['desc']
        request.session['release'] = request.POST['date']
    

        last_tv = models.set_tv(request.session['title'],request.session['network'],request.session['release'])

        return redirect('/shows/'+str(last_tv))
        # return redirect(f'/shows/{last_tv}')


    return redirect('shows/new')

def create_read(request, tv_id):
    special_id = models.special_tv(tv_id)
    context = {
        'id': tv_id,
        'title': special_id.title,
        'network': special_id.network,
        'release': special_id.release_date,
    }

    return render(request, "index3.html", context)