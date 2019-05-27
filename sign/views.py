from django.shortcuts import render, get_object_or_404, redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.
def register(request):
	### request.method = GET代表進入註冊頁面, POST代表提交表單
	if request.method != 'POST':
		form = SignUpForm()
	else:
		form = SignUpForm(data=request.POST)

		if form.is_valid():
			user = form.save()
			authenticated_user = authenticate(username=user.username, password=request.POST['password1'])
			auth.login(request, authenticated_user)
			return HttpResponseRedirect(reverse('home'))
	context = {'form':form}
	return render(request, 'sign/register.html', context)

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('home'))