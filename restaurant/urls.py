from django.urls import path

from . import views

app_name = 'restaurant'
urlpatterns = [
    path('addRestaurant/', views.addRestaurant, name='addRestaurant'),
    path('listRestaurant/', views.listRestaurant, name='listRestaurant'),
]