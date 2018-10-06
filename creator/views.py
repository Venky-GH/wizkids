from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
from .models import course,topic,content

TOPICS = None
CID = None
import json
from django.core.files.storage import FileSystemStorage
def creator(request):
    # displaying the course page!!!
    c = course.objects
    print(c.all)

    return render(request,'creator.html',{'keys':c, 'chk':3})

def topics(request):
    ids = request.GET['foreignKey']
    tops = topic.objects.filter(cid=ids).order_by('oid')
    global TOPICS
    TOPICS = tops
    global CID
    CID = ids
    return render(request,'creator.html',{'keys':tops,'chk':1,'coursekey':ids})

def resource(request):
    ids = request.GET['foreignKey']
    con = content.objects.filter(tid=ids)
    return render(request,'creator.html',{'keys':con,'chk':2,'topicID':ids})

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

def reorder(request):
    global CID,TOPICS
    tops = TOPICS
    s = request.GET['setvalue']
    naam = course.objects.filter(ids=CID)
    recurr(0,s,naam[0])
    print(s)
    # for i in range(0,len(s)):
    #     obj = topic.objects.filter(Q(oid=int(s[i])) & Q(cid=naam[0]))
    #     if len(obj) == 1:
    #         obj[0].oid = i+1
    #         obj[0].save()
    #     else:
    #         obj[1].oid = i+1
    #         obj[1].save()
    #     print(s[i],i+1)
    return render(request, 'creator.html', {'keys':tops, 'chk':1, 'courseID':CID})

def recurr(i,s,naam):
    if(i == len(s)):
        return
    obj = topic.objects.get(Q(oid=int(s[i])) & Q(cid=naam))
    obj.oid = i + 1
    i = i + 1
    print(s[i-1], i)
    recurr(i,s,naam)
    obj.save()


def addRes(request):
    temp = request.POST['resId']
    print(temp)
    naam = topic.objects.filter(ids=request.POST['Fkey'])
    cons = content.objects.filter(tid=request.POST['Fkey'])
    if temp=='1':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        data ={"link":uploaded_file_url}
        dataJson = json.dumps(data)
        details = content(tid=naam[0],code= request.POST['rSelected'],data= dataJson,oid=request.POST['orderid'])
    else:
        # all about text and questions
        ques = request.POST['title']
        ans = request.POST['summary']
        data = {ques:ans}
        dataJson = json.dumps(data)
        details = content(tid=naam[0],code= request.POST['rSelected'],data=dataJson,oid=request.POST['orderid'])
    details.save()
    return render(request,'creator.html',{'keys':cons,'chk':2,'topicID':request.POST['Fkey']})
