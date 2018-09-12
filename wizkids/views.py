from django.shortcuts import render
from feedbacks.models import feedback
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import account


def home(request):
	feeds = feedback.objects
	'''acc = account.objects
				f = list(feeds.all())
				a = list(acc.all())
				for i in range(0,len(f)):
					b = account.objects.filter(userid__exact = f[i].userid)
					print(b)'''
	d = {}
	for feed in feeds.all():
		o = account.objects.get(userid=feed.userid)
		if feed.userid not in d:
			d[feed.userid] = o.username
	print(d[2])
	b = {}
	a = 0
	return render(request, 'home.html', {'feeds' : feeds, 'd' : d, 'b' : a})