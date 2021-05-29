
from django.urls import path
from . import views


urlpatterns = [
    
    path('' , views.show_all),
    path('show' , views.show_tabel),
    path('show/new', views.New_add_show),
    path('create' , views.single_show),
    path('show/<int:id>' , views.show_details),
    path('show/edit/<int:id>' , views.edit_show),
    path('show/update/<int:id>' , views.update_show),
    path('show/delete/<int:id>',views.delete_show),

    
]