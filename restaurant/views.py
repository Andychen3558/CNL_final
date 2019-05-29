from django.shortcuts import render, render_to_response, redirect
from .models import Restaurant
from django.contrib.auth.decorators import login_required
from datetime import timedelta
# Create your views here.

@login_required
def addRestaurant(request):
	if request.method == 'GET':
		return render(request, 'restaurant/addRestaurant.html')
	elif request.method == 'POST':
		restaurant_instance = Restaurant()
		try:
			restaurant_instance.restaurant_name = request.POST['restaurant_name']
			restaurant_instance.phone_number = request.POST['phone_number']
			restaurant_instance.seat_number = request.POST['seat_number']
			restaurant_instance.timeout = timedelta(minutes=int(request.POST['timeout']))
			restaurant_instance.eat_time = timedelta(minutes=int(request.POST['eat_time']))

			if restaurant_instance.restaurant_name == None or \
			restaurant_instance.phone_number == None or \
			restaurant_instance.seat_number == None or \
			restaurant_instance.timeout == None or \
			restaurant_instance.eat_time == None:
				print("Some block are blank.")

			restaurant_instance.save()
		except Exception as e:
			print(e)
		restaurants = Restaurant.objects.all()
		context = {'restaurants':restaurants}
		return redirect('/restaurant/listRestaurant/')
	else:
		restaurants = Restaurant.objects.all()
		context = {'restaurants':restaurants}
		return render(request, 'restaurant/listRestaurant.html', context)

@login_required
def listRestaurant(request):
	restaurants = Restaurant.objects.all()
	context = {'restaurants':restaurants}
	return render(request, 'restaurant/listRestaurant.html', context)