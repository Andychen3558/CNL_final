from django.shortcuts import render
from .models import Restaurant
# Create your views here.

# def addRestaurant(request):
# 	if request.method == 'GET':
# 		restaurant_instance = Restaurant.object.create()
# 		context = {'restaurant_instance':restaurant_instance}
# 		return render(request, 'restaurant/addRestaurant.html', context)
# 	elif request.method == 'POST':
# 		restaurant_instance = Restaurant.object.create(
# 									name=request.POST['name'],
# 									phone_number=request.POST['phone_number']
# 								)
# 		restaurant_instance.save()
# 		restaurants = Restaurant.objects.all()
# 		context = {'restaurants':restaurants}
# 		return render(request, 'restaurant/listRestaurant.html', context)
# 	else:
# 		restaurants = Restaurant.objects.all()
# 		context = {'restaurants':restaurants}
# 		return render(request, 'restaurant/listRestaurant.html', context)

def listRestaurant(request):
	restaurants = Restaurant.objects.all()
	context = {'restaurants':restaurants}
	return render(request, 'restaurant/listRestaurant.html', context)