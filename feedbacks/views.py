from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import feedback
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def course(request):
	return render(request,'course.html')

def feed(request):
	v = request.GET['fb']
	uid = request.user.id
	f = feedback(userid=uid, summary=v)
	f.save()
	return render(request, 'course.html', {'Response' : 'Feedback Submitted Successfully! :)'})
