from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Event, Position
import random

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("path index")

def details(request, token):
    event = Event.objects.get(token=token)
    positions = Position.objects.filter(event=event)
    context = {'event' : event, 'positions' : positions}
    return render(request, 'event_details.json', context)

@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        data = request.POST
        new_event = Event(title=data['title'], token=randToken(), start=data['start'], stop=data['stop'])
        new_event.save()
        context = {'event' : new_event}
        return render(request, 'create_event.json', context)

def randToken():
    a = '123456789abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
    return "".join([random.choice(a) for _ in range(10)])
