from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Event, Comment
from .forms import UploadFileForm
from django.conf import settings
import json, base64, os
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
#import base64

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404, redirect, render

def landingpage(request):
    return render(request, 'landing.html')

@csrf_protect
def home(request):
    c = {}
    events = Event.objects.all().order_by('-pub_date')
    return render(request, 'base.html', {'events':events}, c)

@csrf_protect
def delete_comment(request):
    response = {"code": 500, "message": "request worked"}
    try:
        data = json.loads(request.body.decode("utf-8"))
        c_id = int(data[u'id'])
        Comment.objects.get(id=c_id).delete()
        print("DELETED")
        response["code"] = 200
    except Exception as e:
        response["error"] = str(e)
        response["message"] = "failed"
        print(str(e))
    return JsonResponse(response)

@csrf_protect
def add_comment(request):
    response = {"code": 500, "message": "request failed to execute"}
    try:
        data = json.loads(request.body.decode("utf-8"))
        text = str(data[u'comment'])
        e_id = int(data[u'event_id'])
        event = Event.objects.get(id=e_id)
        comment = Comment(comment_text=text, event_id=event, comment_author=request.user)
        comment.save()
        response["code"] = 200
        response["id"] = comment.id
        response["message"] = "Success"
        print("SAVED")
    except Exception as e:
        response["error"] = str(e)
        print(str(e))
    return JsonResponse(response)

@csrf_protect
def eventForm(request, eventid):
    c = {}
    print("type"+str(type(eventid)))
    event = Event.objects.get(id=eventid)
    filename = event.event_form
    try:
        comments = Comment.objects.filter(event_id=event).order_by('-published_date')
    except Exception:
        comments = None
    return render(request, 'eventform.html', {'event':event,'filename':filename, 'comments':comments}, c)

@csrf_protect
def eventpage(request):
    c = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES.get('input-b1')
            if filename != None:
                filename = filename.name
                path = os.path.join(settings.BASE_DIR, 'static', "uploads/"+filename)
                path = str(path.replace(" ",""))
                handle_uploaded_file(request.FILES['input-b1'],path)
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'eventpage.html', {'form':form}, c)

def handle_uploaded_file(f,path):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_protect
def createEvent(request):
    
    response = {"code": 500, "message": "request failed to send"}
    
    try:
        data = json.loads(request.body.decode("utf-8"))
        filename = str(data.get(u'filename'))
        if filename == None or filename == "None":
            path = "https://i.pinimg.com/originals/9b/87/0b/9b870b29291ee7502d0ec99ab3b6733d.png"
        else:
            path = "../static/uploads/" + filename
            path_form = "/static/uploads/" + filename
            path = str(path.replace(" ",""))
            path_form = str(path_form.replace(" ",""))

        newEvent = Event(event_title= str(data[u'title']), event_date=str(data[u'date']), event_info=str(data[u'additional_info']), 
            event_time= str(data[u'time']), event_street= str(data[u'street']), event_city= str(data[u'city']), 
            event_zip= str(data[u'zip']), event_form=path_form, event_user= request.user, category= str(data[u'category']),reader= path,)
        
        newEvent.save()
        print("Saved")
        response["code"] = 200
        response["message"] = "success"  
    except Exception as e:
        response["error"] = str(e)
        print(str(e))
    
    return JsonResponse(response)


@csrf_protect
def delete_event(request):
    response = {"code":500,"message":"request failed to execute"}
    try:
        data = json.loads(request.body.decode("utf-8"))
        e_id = int(data[u'id'])
        Event.objects.get(id=e_id).delete()
        response["code"] = 200
        response["message"] = "Success"
        response["url"] = reverse('home')
    except Exception as e:
        response["error"] = str(e)
        print(str(e))
    return JsonResponse(response)



# @login_required
# def event(request, pk):
#     board = get_object_or_404(Event, pk=pk)
#     if request.method == 'POST':
        
