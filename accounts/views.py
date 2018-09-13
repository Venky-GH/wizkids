from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import account
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def signup(request):
	if request.method == 'POST':
		if request.POST['pass1'] == request.POST['pass2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'login.html', {'Error' : 'Username has already been taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['pass2'])
				u = User.objects.get(username=request.POST['username'])
				uploaded_file_url = model_form_upload(request)
				acc = account(username=User.objects.get(username=request.POST['username']), parentname=request.POST['parent'], childname=request.POST['child'], email=request.POST['email'], userid=u.id, image=uploaded_file_url)
				acc.save()
				
				auth.login(request, user)
				return redirect('home')	
		else:
			return render(request, 'home.html', {'Error' : 'Passwords Do not match'})
	else:
		return render(request, 'login.html')


def model_form_upload(request):
	myfile = request.FILES['myfile']
	fs = FileSystemStorage()
	filename = fs.save(myfile.name, myfile)
	uploaded_file_url = fs.url(filename)
	return uploaded_file_url
	#return HttpResponse('Uploaded successfully')


def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'],password=request.POST['pass'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'home.html', {'Error' : 'Invalid Credentials'})
	else:
		return render(request, 'home.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')


