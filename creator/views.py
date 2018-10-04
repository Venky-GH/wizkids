from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import course,topic,content

def creator(request):
    # displaying the course page!!!
    c = course.objects
    print(c.all)
    
    return render(request,'creator.html',{'keys':c})

def topics(request):
    ids = request.GET['foreignKey']
    tops = topic.objects.filter(cid=ids)

    return render(request,'creator.html',{'keys':tops,'chk':1})

def resource(request):
    ids = request.GET['foreignKey']
    con = content.objects.filter(tid=ids)
    return render(request,'creator.html',{'keys':con,'chk':2})