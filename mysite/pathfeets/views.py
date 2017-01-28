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
