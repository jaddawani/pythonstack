
from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.index),
    path('register' ,views.register),
    path('favorite', views.favorite),
    path('login' , views.login),
    path('logout' , views.logout),
    path('add_book' , views.add_book),
    path('book/<int:id>' , views.show_book),
    path('book/delete/<int:id>',views.delete_show),
    path('book/update/<int:id>' , views.update_show),
    path('book/fav/<int:id>' , views.add_fav),
    path('book/unfav/<int:id>' , views.remove_fav)
    
]
