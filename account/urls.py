from django.urls import path
from django.contrib import admin

from .views import login_view, logout_view


# URL's account app
urlpatterns = [
	path('login/', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
]