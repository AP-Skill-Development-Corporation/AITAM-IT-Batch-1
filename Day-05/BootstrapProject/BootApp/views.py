from django.shortcuts import render

# Create your views here.
def home(r):
	return render(r,'html/home.html')

def about(request):
	return render(request,'html/abt.html')

def contact(request):
	return render(request,'html/ct.html')