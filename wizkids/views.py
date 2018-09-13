from django.shortcuts import render
from feedbacks.models import feedback
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import account


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
	return render(request, 'home.html', {'d' : d})