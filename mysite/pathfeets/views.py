from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Event, Position, PlannedPosition
from datetime import datetime
from .models import Event, Position, PlannedPosition
import random
from django.core import serializers
import pusher

pusher_client = pusher.Pusher(
  app_id='295609',
  key='e063970a13a7cd349f09',
  secret='9677abe4331996b7670f',
  cluster='eu',
  ssl=True
)

def index(request):
    return HttpResponse("needs to be made")

def event(request, token):
    event = Event.objects.get(token=token)
    planned = PlannedPosition.objects.filter(event=event)

    context = {'event':event, 'planned':planned}
    return render(request, 'index.html', context)

def details(request, token):
    event = Event.objects.get(token=token)
    positions = Position.objects.filter(event=event).order_by('timestamp', 'pk')
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
    a = '0123456789abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
    return "".join([random.choice(a) for _ in range(10)])

def receive_gps_coord(request):
    data = request.POST

    event_id = data['event_id']
    event = Event(id=event_id)
    pos = Position(event=event, latitude=data['latitude'], longtitude=data['longtitude'], timestamp=datetime.now())
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

    return HttpResponse(str(planned_pos.id));

@csrf_exempt
def delete_planned_pos(request):
    data = request.POST
    planned_pos = PlannedPosition(id=int(data['id']))
    planned_pos.delete()

    return HttpResponse("")

@csrf_exempt
def new_chat_msg(request):
    data = request.POST

    pusher_client.trigger('my-channel', str(data['id']), {'message': data['msg']})

    return HttpResponse("")
