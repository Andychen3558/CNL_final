from django.shortcuts import render, render_to_response, redirect
from .models import Restaurant
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.contrib.auth.models import User
from users.models import CustomUser
import datetime
from .module import wait_time
# Create your views here.

class res():

	def __init__(self, name, phone, seat, waiting_queue, wait_time='', dining_queue=''):

		self.name = name
		self.phone = phone
		self.seat = seat
		self.wait_time = wait_time
		self.waiting_queue_client = [waiting_queue[i].split('/')[0] for i in range(1, len(waiting_queue))]
		self.waiting_queue_phone_number = [waiting_queue[i].split('/')[1] for i in range(1, len(waiting_queue))]
		self.dining_queue_client = [dining_queue[i].split('/')[0] for i in range(1, len(dining_queue))]


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
		context = {}
		if restaurant_instance.exists():
			restaurant_instance = restaurant_instance[0]
			print(restaurant_instance.restaurant_name)
			r = res(restaurant_instance.restaurant_name, 
				restaurant_instance.phone_number, 
				restaurant_instance.seat_number, 
				restaurant_instance.waiting_queue.split('||'),
				dining_queue=restaurant_instance.dining_queue.split('||'),
				)
			context['r'] = r
		context['restaurant'] = restaurant_instance
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
			restaurant_instance.dining_time_average = timedelta(minutes=timeString2Minute(request.POST['eat_time'])).total_seconds() / 60

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
	waitTimelist = []

	for restaurant in restaurants:
		print("restaurant:", restaurant.waiting_queue.split("||"))	
		wait_list = []
		timeout=restaurant.timeout.total_seconds() / 60
		skipprob=restaurant.skip_probability
		client_names = []

		for client_info in restaurant.waiting_queue.split('||'):
			if len(client_info) == 0:
				continue
			client_names.append(client_info.split('/')[0])
		UserArrivalTime = [CustomUser.objects.get(username=name).arrival_time.total_seconds() / 60 for name in client_names]
		AverageDiningTime = restaurant.dining_time_average
		TableNum = restaurant.seat_number
		print("AverageDiningTime:{}".format(AverageDiningTime))
		wait_list = wait_time.waiting_time_evaluate(timeout, skipprob, UserArrivalTime, AverageDiningTime, TableNum)
		print("Evaluate average waiting time:{}".format(wait_list))
		waitTimelist.append(wait_list)

	count = 0
	for restaurant_instance in restaurants:
		r.append(res(restaurant_instance.restaurant_name, 
			restaurant_instance.phone_number, 
			restaurant_instance.seat_number, 
			restaurant_instance.waiting_queue.split('||'), 
			wait_time=waitTimelist[count]))
		count += 1
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
	restaurant_instance.reservation_total_num += 1
	restaurant_instance.save()
	print(restaurant_instance.waiting_queue)
	return redirect('/restaurant/listRestaurant/')

@login_required
def takeSeat(request, reserve_restaurant_name):
	restaurant_instance = Restaurant.objects.get(restaurant_name=reserve_restaurant_name)
	if len(restaurant_instance.waiting_queue) == 0:
		return redirect("/restaurant/addRestaurant/")
	idx = restaurant_instance.waiting_queue[2:].find('||')
	takeSeat_client = ''
	if idx == -1:
		takeSeat_client = restaurant_instance.waiting_queue
		restaurant_instance.dining_queue += restaurant_instance.waiting_queue
		restaurant_instance.waiting_queue = ''
	else:
		takeSeat_client = restaurant_instance.waiting_queue[:idx+2]
		restaurant_instance.waiting_queue = restaurant_instance.waiting_queue[idx+2:]
		restaurant_instance.dining_queue += takeSeat_client
		print('takeSeat_client: ', takeSeat_client)
	takeSeat_client = takeSeat_client[2:].split("/")[0]
	dining_info = "||" + takeSeat_client + "/" + datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
	restaurant_instance.dining_time +=  dining_info
	# print(restaurant_instance.dining_time)
	print("dining_time:", restaurant_instance.dining_time)

	######### this need to be used to count average waiting time
	##### 單一一位客人延遲時間 = user.arrival_time
	if restaurant_instance.coming_time != "":
		lag_time = datetime.datetime.now() - datetime.datetime.strptime(restaurant_instance.coming_time, "%Y:%m:%d:%H:%M:%S")
		lag_time = wait_time.update_arrivetime(request.user.arrival_time.total_seconds(), lag_time.total_seconds())
		lag_time = timedelta(seconds=lag_time)
		uu = request.user
		uu.arrival_time = lag_time
		uu.save()
		print("Name:{} lag_time:{}".format(uu.username, uu.arrival_time))
		print(lag_time)

	restaurant_instance.save()
	print('waiting_queue:', restaurant_instance.waiting_queue)
	return redirect('/restaurant/addRestaurant/')
	
@login_required
def skip(request, reserve_restaurant_name):
	restaurant_instance = Restaurant.objects.get(restaurant_name=reserve_restaurant_name)
	if len(restaurant_instance.waiting_queue) == 0:
		return redirect("/restaurant/addRestaurant/")
	idx = restaurant_instance.waiting_queue[2:].find('||')
	if idx == -1:
		restaurant_instance.waiting_queue = ''
	else:
		restaurant_instance.waiting_queue = restaurant_instance.waiting_queue[idx+2:]
	restaurant_instance.reservation_skip_num += 1
	restaurant_instance.save()
	print('waiting_queue:', restaurant_instance.waiting_queue)
	return redirect('/restaurant/addRestaurant/')

@login_required
def eatFinish(request, client_name, reserve_restaurant_name):
	restaurant_instance = Restaurant.objects.get(restaurant_name=reserve_restaurant_name)
	print('dining_queue: ', restaurant_instance.dining_queue)
	idx_name = restaurant_instance.dining_queue.find(client_name)
	idx_next_bound = restaurant_instance.dining_queue[idx_name:].find('||')
	if idx_next_bound == -1:
		restaurant_instance.dining_queue = restaurant_instance.dining_queue[:idx_name - 2]
	else:
		restaurant_instance.dining_queue = restaurant_instance.dining_queue[:idx_name - 2] + restaurant_instance.dining_queue[idx_name + idx_next_bound:]
	
	restaurant_client_num = len([client for client in restaurant_instance.dining_queue.split("||") if client != ""])
	if restaurant_client_num == restaurant_instance.seat_number - 1 and restaurant_instance.waiting_queue != "":
		restaurant_instance.coming_time = datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
		print("coming_time:", restaurant_instance.coming_time)

	##### this part is for caculating eating time

	leftbound = restaurant_instance.dining_time.find(client_name)
	rightbound = restaurant_instance.dining_time[leftbound:].find("||")
	info = ''
	if rightbound == -1:
		info = restaurant_instance.dining_time[leftbound:]
		restaurant_instance.dining_time = restaurant_instance.dining_time[:leftbound - 2]
	else:
		info = restaurant_instance.dining_time[leftbound:rightbound+leftbound]
		restaurant_instance.dining_time = restaurant_instance.dining_time[:leftbound - 2] + restaurant_instance.dining_time[leftbound+rightbound:]
	print("info:", info)
	cur_eattime = datetime.datetime.now() - datetime.datetime.strptime(info.split('/')[1], "%Y:%m:%d:%H:%M:%S")
	eattime_inMin = cur_eattime.total_seconds() / 60
	print("this client eat:{} min".format(eattime_inMin))
	restaurant_instance.dining_time_average = (restaurant_instance.dining_time_average * restaurant_instance.dining_total_num + eattime_inMin) / ( restaurant_instance.dining_total_num + 1)
	restaurant_instance.dining_total_num += 1
	print("timeaverage, total_num")
	print(restaurant_instance.dining_time_average, restaurant_instance.dining_total_num)

	restaurant_instance.save()

	print(client_name)
	print(reserve_restaurant_name)
	print('dining_queue: ', restaurant_instance.dining_queue)
	return redirect('/restaurant/addRestaurant/')
