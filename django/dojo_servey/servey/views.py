
from django.http import request
from django.shortcuts import redirect, render , HttpResponse


def index(requests):
    return render(requests, "index.html")

def hello(requests):
    name=requests.POST["name"]
    email=requests.POST["email"]
    location=requests.POST["location"]
    language=requests.POST["language"]
    comments=requests.POST["comments"]

    dict={
        "name": name,
        "email": email,
        "location": location,
        "language": language,
        "comments" : comments
        



    }
    return render(requests, "hello.html", dict)

