from django.urls import path, include
from . import views

urlpatterns = [
    path('' , views.index),
    path('shows' , views.index2),
    path("shows/new", views.show),
    path("create", views.create_tv),
    path('shows/<tv_id>', views.create_read),

    
]