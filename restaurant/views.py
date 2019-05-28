from django.shortcuts import render, render_to_response
from .models import Restaurant
# Create your views here.

def addRestaurant(request):
	if request.method == 'GET':
		return render(request, 'restaurant/addRestaurant.html')
	elif request.method == 'POST':
		restaurant_instance = Restaurant.object.create(
									restaurant_name=request.POST['restaurant_name'],
									phone_number=request.POST['phone_number']
								)
		restaurant_instance.save()
		restaurants = Restaurant.objects.all()
		context = {'restaurants':restaurants}
		return render_to_response('restaurant/listRestaurant.html', context, context_instance=RequestContext(request))
		# return render(request, 'restaurant/listRestaurant.html', context)
	else:
		restaurants = Restaurant.objects.all()
		context = {'restaurants':restaurants}
		return render(request, 'restaurant/listRestaurant.html', context)

def listRestaurant(request):
	restaurants = Restaurant.objects.all()
	context = {'restaurants':restaurants}
	return render(request, 'restaurant/listRestaurant.html', context)