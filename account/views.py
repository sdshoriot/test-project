from django.shortcuts import render
from django.shortcuts import redirect

from .forms import UserLoginForm

from django.contrib.auth import (
	authenticate,
	login,
	logout
)


# Login_view
def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('/')	
	return render(request, 'account/login.html', {'form': form})


# Logout_view
def logout_view(request):
	logout(request)
	return redirect('/')