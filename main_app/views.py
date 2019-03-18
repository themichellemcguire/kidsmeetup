from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Event
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class EventList(LoginRequiredMixin, ListView):
    model = Event

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'
    success_url = '/events/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventUpdate(UpdateView):
    model=Event
    fields = '__all__'

class EventDelete(DeleteView):
    model=Event
    success_url = '/events/'


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

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile/profile.html')

def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events':events})

def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {'event': event})