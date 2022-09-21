from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse("Welcome")

def sa(request,y):
	return HttpResponse("Welcome {}".format(y))

def mn(request,h,u):
	return HttpResponse("Welcome user {} entered age is: {}".format(h,u))


