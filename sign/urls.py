from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'sign'
urlpatterns = [
	# /register
	path('register/', views.register, name='register'),
	# /login
	path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
	# /logout
	path('logout/', views.logout, name='logout'),
]