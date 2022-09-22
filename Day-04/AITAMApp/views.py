from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse("Welcome")

def sa(request,y):
	return HttpResponse("Welcome {}".format(y))

def mn(request,h,u):
	return HttpResponse("Welcome user {} entered age is: {}".format(h,u))

def sk(request,n):
	return HttpResponse("<h1>Welcome {}</h1>".format(n))

def mku(request,d,j):
	return HttpResponse("Welcome user <span style='color:red'>{}</span> entered age is: <span style='color:yellow'>{}</span>".format(d,j))

def gj(request):
	return HttpResponse("<html><head><title>Sample</title></head><body><h1>Welcome to Sample Html Page</h1></body></html>")

def pt(request):
	return render(request,'demo.html')

def register(request):
	return render(request,'ht/regis.html')

