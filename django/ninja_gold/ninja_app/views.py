from django.http import request
from django.shortcuts import redirect, render
import random 


def index(request):

    if "score" in request.session:
        score = request.session["score"] 

    else:
        request.session["score"] = 0
        score = request.session["score"] 

    if "activity" in request.session:
        activity = request.session["activity"] 

    else:
        request.session["activity"] = []
        activity = request.session["activity"] 


    


    

    dict = {
      
       'score' : score ,
       'activity' : activity
      
    }

    return render(request , "index.html", dict )

def index2(request):
   
    if request.POST['forms'] == "farm" : 
       randx= random.randint(10,20)
       request.session['score']+=randx
       request.session["activity"].append(f"you have earned {randx} from farm")
       print(request.session["activity"])
       



    if request.POST['forms'] == "cave" : 
       randx= random.randint(5,10)
       request.session['score']+=randx
       request.session["activity"].append(f"you have earned {randx} from cave")
       print(request.session["activity"])


    if request.POST['forms'] == "House":
        randx= random.randint(2,5)
        request.session['score']+=randx
        request.session['activity'].append(f"you have earned  {randx} from House")


    if request.POST['forms'] == "Casino":
        randx= random.randint(-50,50)
        request.session['score']+=randx
        if randx > 0 :
            request.session['activity'].append(f"you have earned  {randx} from casino")
        if randx < 0 :
            request.session['activity'].append(f"you have LOST!  {randx} from casino")
    return redirect('/')

def index3 (request):

    request.session.clear()
    return redirect('/')


        

    



   

    