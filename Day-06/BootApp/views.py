from django.shortcuts import render,redirect
from .forms import Usreg
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def home(r):
	return render(r,'html/home.html')

def about(request):
	return render(request,'html/abt.html')

def contact(request):
	return render(request,'html/ct.html')

def register(request):
	if request.method == "POST":
		p = Usreg(request.POST)
		if p.is_valid():
			p.save()
			messages.success(request,"User Created Successfully")
			return redirect('/login')
	p = Usreg()
	return render(request,'html/regis.html',{'k':p})

