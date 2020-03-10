from django.shortcuts import render


# Home_page_view
def home(request):
	return render(request, 'home/home.html')