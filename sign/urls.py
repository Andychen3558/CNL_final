from django.urls import path

from . import views

app_name = 'sign'
urlpatterns = [
	path('signUp', views.signUp, name='signUp'),
	path('signIn', views.signIn, name='signIn'),
	# /login/
	path('login/', views.login, name='login'),
	# /register
	path('register/', views.register, name='register'),
]