from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        return HttpResponse('data is submitted')
    return render(request,'login.html')

def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')



    return render(request,'insert_topic.html')
def insert_webpage(request):
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['na']
        url=request.POST['ul']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(name=name)[0]
        WO.save()
        WO=Webpage.objects.get_or_create(url=url)[0]
        WO.save()
        return HttpResponse('Insertion of Webpage is Done')
    
    return render(request,'insert_webpage.html')

def insert_access(request):
    if request.method=='POST':
        name=request.POST['name']
        date=request.POST['dt']
        author=request.POST['au']

        ACO=AcessRecord.objects.get_or_create(name=name)[0]
        ACO.save()
        ACO1=AcessRecord.objects.get_or_create(date=date)[0]
        ACO1.save()

        ACO2=AcessRecord.objects.get_or_create(author=author)[0]
        ACO2.save()
        return HttpResponse('Insertion of Access is Done')
    
    return render(request,'insert_access.html')














