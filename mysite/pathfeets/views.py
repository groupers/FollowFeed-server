from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Event, Position

def index(request):
    return HttpResponse("path index")

def details(request, token):
    event = Event.objects.get(token=token)
    positions = Position.objects.filter(event=event)
    context = {'event' : event, 'positions' : positions}
    return render(request, 'event_details.json', context)
    # return HttpResponse(str([(e.timestamp, e.longitude, e.latitude) for e in positions]))

def receive_gps_coord(request):
	data = request.POST

	event_id = data['event_id']
	event = Event(id=event_id)
	pos = Position(event=event, latitude=data['latitude'], longtitude=data['longtitude'])
	pos.save()

	return HttpResponse("Success");
