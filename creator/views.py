from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import course,topic,content

def creator(request):
    # displaying the course page!!!
    c = course.objects
    print(c.all)

    return render(request,'creator.html',{'keys':c, 'chk':3})

def topics(request):
    ids = request.GET['foreignKey']
    tops = topic.objects.filter(cid=ids)

    return render(request,'creator.html',{'keys':tops,'chk':1,'coursekey':ids})

def resource(request):
    ids = request.GET['foreignKey']
    con = content.objects.filter(tid=ids)
    return render(request,'creator.html',{'keys':con,'chk':2})

def addcourse(request):
    temp = request.POST['pickachu']
    if temp == '1':
        naam = course.objects.filter(ids=request.POST['getcid'])
        tops = topic.objects.filter(cid=request.POST['getcid'])
        details = topic(cid=naam[0],title=request.POST['ctitle'],desc=request.POST['cdesc'],oid=request.POST['orderid'])
        details.save()
        return render(request,'creator.html',{'keys':tops, 'chk':1, 'courseID':request.POST['getcid']})
    else:
        details = course(title=request.POST['ctitle'],desc=request.POST['cdesc'])
        details.save()
        return creator(request)
