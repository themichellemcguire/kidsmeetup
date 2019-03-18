from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Event
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return HttpResponse('<h1>Kids Meetup Home</h1>')


class EventList(LoginRequiredMixin, ListView):
    model = Event


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('events_list')
        else:
            error_message='Invalid credentials: Try again'
    form=UserCreationForm()
    context={'form': form,'error_message':error_message}
    return render(request, 'registration/signup.html',context)

