from django.shortcuts import render, render_to_response, redirect
from .models import Restaurant
# Create your views here.

def addRestaurant(request):
	if request.method == 'GET':
		return render(request, 'restaurant/addRestaurant.html')
	elif request.method == 'POST':
		print('!!!!!!', request.POST['restaurant_name'])
		restaurant_instance = Restaurant.objects.create(
									restaurant_name=request.POST['restaurant_name'],
									# phone_number=request.POST['phoneNumber'],
								)
		restaurant_instance.save()
		restaurants = Restaurant.objects.all()
		context = {'restaurants':restaurants}
		return redirect('/restaurant/listRestaurant/')
		# return render(request, 'restaurant/listRestaurant.html', context)
	else:
		restaurants = Restaurant.objects.all()
		context = {'restaurants':restaurants}
		return render(request, 'restaurant/listRestaurant.html', context)

def listRestaurant(request):
	restaurants = Restaurant.objects.all()
	context = {'restaurants':restaurants}
	return render(request, 'restaurant/listRestaurant.html', context)