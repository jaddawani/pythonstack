
from django.urls import path
from . import views

urlpatterns = [
    path('',views.countt),
    path('deleted',views.clears)
]
