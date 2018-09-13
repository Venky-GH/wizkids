from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
	path('', views.course, name='course'),
	url(r'^GET', views.feed, name='feed'),
	path('abc/',views.subs,name='subs')
] 
