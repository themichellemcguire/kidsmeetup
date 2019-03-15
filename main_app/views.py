from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Event

# Create your views here.

def home(request):
    return HttpResponse('<h1>Kids Meetup Home</h1>')

class EventList(ListView):
    model = Event

