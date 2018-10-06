from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
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
    l = len(tops)+1
    #todo : order id hidden and prefillled
    global TOPICS
    TOPICS = tops
    global CID
    CID = ids
    return render(request,'creator.html',{'keys':tops,'chk':1,'courseID':ids,'ordLen':l})

def resource(request):
    ids = request.GET['foreignKey']
    con = content.objects.filter(tid=ids)
    l = len(con)+1
    #todo : order id hidden and prefillled
    return render(request,'creator.html',{'keys':con,'chk':2,'topicID':ids,'topOrdLen':l})

def addcourse(request):
    temp = request.POST['pickachu']
    if temp == '1':
        naam = course.objects.filter(ids=request.POST['getcid'])
        tops = topic.objects.filter(cid=request.POST['getcid'])
        details = topic(cid=naam[0],title=request.POST['ctitle'],desc=request.POST['cdesc'],oid=request.POST['orderid'])
        details.save()
        oid = int(request.POST['orderid'])+1
        return render(request,'creator.html',{'keys':tops, 'chk':1, 'courseID':request.POST['getcid'],'ordLen':oid})
    else:
        details = course(title=request.POST['ctitle'],desc=request.POST['cdesc'])
        details.save()
        return creator(request)


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
    oid = int(request.POST['orderid'])+1
    return render(request,'creator.html',{'keys':cons,'chk':2,'topicID':request.POST['Fkey'],'topOrdLen':oid}) 

    
def reorder(request):
    global CID,TOPICS
    tops = TOPICS
    return render(request, 'creator.html', {'order':1, 'keys':tops, 'chk':1, 'courseID':CID})
