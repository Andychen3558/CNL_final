from django.shortcuts import render, get_object_or_404, redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def signUp(request):
	return render(request, 'sign/sign.html', {'isLogin':False})

def signIn(request):
	return render(request, 'sign/sign.html', {'isLogin':True})	

def register(request):
	username = request.POST['username']
	try:
		user = User.objects.get(username=username)
	except:
		user = None
	if user != None:
		msg = "帳號已經註冊！"
		return redirect('/')
		#return render(request, 'home.html', {'user':user})
	# else:
	# 	user = User.objects.create_user("")

def login(request):
	username = request.POST['username']