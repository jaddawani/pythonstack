
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('register' ,views.register),
    path('main_wall', views.main_wall),
    path('login' , views.login),
    path('logout' , views.logout),
    path('add_message' , views.add_message),
    path('add_comment' , views.add_comment)
   
]