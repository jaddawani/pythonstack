from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    
    path('',views.index),
    path("book",views.index2),
    path("views/<int:x>", views.index3),


]

