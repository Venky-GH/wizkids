from django.shortcuts import render
from feedbacks.models import feedback
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import account


def access_denied(request):
	return render(request, 'access_denied_403.html')

def home(request):
	feeds = feedback.objects
	d = {}
	i=0
	for feed in reversed(feeds.all()):
		if i<6:
			o = account.objects.get(userid=feed.userid)
			#d[o.username] = feed.summary
			d[o.username] = {}
			d[o.username][feed.summary] = o.image
			i+=1

	print(d)
	curruser = None
	if request.user.id:
		curruser = request.user.id
	return render(request, 'home.html', {'d' : d, 'currentUser' : curruser})

def show_test(request):
	return render(request, 'index.html')
