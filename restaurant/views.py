from django.shortcuts import render, render_to_response, redirect
from .models import Restaurant
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.contrib.auth.models import User
# Create your views here.

class res():

	def __init__(self, name, phone, seat, waiting_queue):

		self.name = name
		self.phone = phone
		self.seat = seat
		self.waiting_queue = [waiting_queue[i].split('/')[0] for i in range(1, len(waiting_queue))]


def timeString2Minute(timeString):
	print(timeString2Minute)
	times = timeString.split(':')
	if len(times) == 1:
		return int(timeString)
	elif len(times) == 3:
		return int(times[0])*60 + int(times[1])
	else:
		return 30

@login_required
def addRestaurant(request):
	if request.method == 'GET':
		name = request.user.username
		restaurant_instance = Restaurant.objects.filter(created_by=request.user)
		if restaurant_instance.exists():
			restaurant_instance = restaurant_instance[0]
			print(restaurant_instance.restaurant_name)
		context = {'restaurant':restaurant_instance}
		return render(request, 'restaurant/addRestaurant.html', context)
	elif request.method == 'POST':
		restaurant_instance = Restaurant.objects.filter(created_by=request.user)
		if restaurant_instance.exists():
			print(restaurant_instance)
			restaurant_instance = restaurant_instance[0]
		else:
			restaurant_instance = Restaurant()
		try:
			restaurant_instance.created_by = request.user
			restaurant_instance.restaurant_name = request.POST['restaurant_name']
			restaurant_instance.phone_number = request.POST['phone_number']
			restaurant_instance.seat_number = request.POST['seat_number']
			restaurant_instance.timeout = timedelta(minutes=timeString2Minute(request.POST['timeout']))
			restaurant_instance.eat_time = timedelta(minutes=timeString2Minute(request.POST['eat_time']))

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
	r = []
	for restaurant_instance in restaurants:
		r.append(res(restaurant_instance.restaurant_name, restaurant_instance.phone_number, restaurant_instance.seat_number, restaurant_instance.waiting_queue.split('||')))
	context = {'restaurants':r}
	return render(request, 'restaurant/listRestaurant.html', context)

@login_required
def makeReserve(request, reserve_restaurant_name):
	restaurant_instance = Restaurant.objects.get(restaurant_name=reserve_restaurant_name)
	# print(restaurant_instance.phone_number)
	for client_info in restaurant_instance.waiting_queue.split('||'):
		if client_info == '':
			continue
		if client_info.split('/')[0] == request.user.username:
			print(restaurant_instance.waiting_queue)
			return redirect('/restaurant/listRestaurant/')
	restaurant_instance.waiting_queue += '||%s/%s'%(request.user.username, request.user.phone_number)
	restaurant_instance.save()
	print(restaurant_instance.waiting_queue)
	return redirect('/restaurant/listRestaurant/')
