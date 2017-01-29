from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Event, Position, PlannedPosition
from datetime import datetime

def index(request):
    return HttpResponse("path index")

def details(request, token):
    event = Event.objects.get(token=token)
    positions = Position.objects.filter(event=event)
    context = {'event' : event, 'positions' : positions}
    return render(request, 'event_details.json', context)

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
				timestamp=datetime.strptime(data['timestamp'], r'%Y-%m-%d %H:%M'),
				longitude=data['longitude'], latitude=data['latitude'])
	planned_pos.save()

	return HttpResponse("Success");
