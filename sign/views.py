from django.shortcuts import render, get_object_or_404, redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			user = form.save()
			authenticated_user = authenticate(username=user.username, password=request.POST['password1'])
			auth.login(request, authenticated_user)
			return HttpResponseRedirect(reverse('home'))
	context = {'form':form}
	return render(request, 'sign/register.html', context)

def logout(request):
	auth.logout(request)
	return redirect('/')