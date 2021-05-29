
from django.urls import path
from . import views



urlpatterns = [
    
    path('' , views.book),
    path('add' , views.addbook),
    path('shows/<int:id>' , views.showbook),
    path('addAuthorToBook', views.AuthorToBook)
]
