"""AITAMProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AITAMApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('df/',views.demo),
    path('g/<str:y>/',views.sa),
    path('k/<str:h>/<int:u>/',views.mn),
    path('dm/<str:n>/',views.sk),
    path('w/<str:d>/<int:j>/',views.mku),
    path('gh/',views.gj),
    path('ty/',views.pt),
    path('rg/',views.register),
]
