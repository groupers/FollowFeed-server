from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Event, Position, PlannedPosition
from datetime import datetime
from .models import Event, Position, PlannedPosition
import random
from django.core import serializers

def index(request):
    return HttpResponse("needs to be made")

def event(request, token):
    event = Event.objects.get(token=token)
    planned = PlannedPosition.objects.filter(event=event)

    context = {'event':event, 'planned':planned}
    return render(request, 'index.html', context)

def details(request, token):
    event = Event.objects.get(token=token)
    positions = Position.objects.filter(event=event)
    context = {'event' : event, 'positions' : positions}
    return render(request, 'event_details.json', context)

@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        data = request.POST
        new_event = Event(title=data['title'], token=randToken(), start=datetime.strptime(data['start'], r'%Y-%m-%d %H:%M'), stop=datetime.strptime(data['stop'], r'%Y-%m-%d %H:%M'))
        new_event.save()
        context = {'event' : new_event}
        return render(request, 'create_event.json', context)

def randToken():
    a = '123456789abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
    return "".join([random.choice(a) for _ in range(10)])
    # return HttpResponse(str([(e.timestamp, e.longitude, e.latitude) for e in positions]))

def receive_gps_coord(request):
    data = request.POST

    event_id = data['event_id']
    event = Event(id=event_id)
    pos = Position(event=event, latitude=data['latitude'], longtitude=data['longtitude'])
    pos.save()

    return HttpResponse("Success");

@csrf_exempt
def make_planned_pos(request):
    data = request.POST

    event_id = data['event_id']
    event = Event(id=event_id)
    planned_pos = PlannedPosition(event=event, title=data['title'],
                timestamp=datetime.strptime(data['timestamp'], r'%Y-%m-%d %H:%M:%S'),
                longitude=data['longitude'], latitude=data['latitude'])
    planned_pos.save()

    return HttpResponse("Success");
