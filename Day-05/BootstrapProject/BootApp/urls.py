from django.urls import path
from BootApp import views

urlpatterns = [
	path('',views.home,name='hm'),
	path('aboutpage/',views.about,name='ab'),
	path('cont/',views.contact,name='cnt'),
]