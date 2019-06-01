from django.urls import path

from . import views

app_name = 'restaurant'
urlpatterns = [
    path('addRestaurant/', views.addRestaurant, name='addRestaurant'),
    path('listRestaurant/', views.listRestaurant, name='listRestaurant'),
    path('makeReserve/<str:reserve_restaurant_name>', views.makeReserve, name='makeReserve'),
    path('takeSeat/<str:reserve_restaurant_name>', views.takeSeat, name='takeSeat'),
    path('skip/<str:reserve_restaurant_name>', views.skip, name='skip'),
    path('eatFinish/<str:client_name>&<str:reserve_restaurant_name>', views.eatFinish, name='eatFinish'),
]