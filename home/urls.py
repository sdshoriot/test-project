from django.contrib import admin
from django.urls import path

from .views import home

# URL's home app
urlpatterns = [
	path('', home, name='home'),  
]