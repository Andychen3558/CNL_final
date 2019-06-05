from django.shortcuts import render, render_to_response
from restaurant.models import Restaurant

def home(request):
	restaurants = Restaurant.objects.all()
	return render(request, 'home.html', {'restaurants':restaurants})