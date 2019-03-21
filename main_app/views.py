from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Event, Child
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  UserForm,ParentForm 
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


class EventList(ListView):
    model = Event


class EventDetail(LoginRequiredMixin, DetailView):
    model = Event

@login_required
def events_detail(request, event_id):
  event = Event.objects.get(id=event_id)
  # Get the toys the cat doesn't have
  childs_event_doesnt_have = Child.objects.exclude(id__in = event.childs.all().values_list('id')).filter(user=request.user)
  # Instantiate FeedingForm to be rendered in the template
  c=childs_event_doesnt_have
  
  print(c)

  return render(request, 'main_app/event_detail.html', {
    # Pass the cat and feeding_form as context
    'event': event, 
    # Add the toys to be displayed
    'childs': childs_event_doesnt_have
  })

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = [
        'name',
        'address',
        'date'
    ]
    
    def form_valid(self, form):
        form.instance.user = self.request.user

        form.instance.parent=self.request.user.parent
        return super().form_valid(form)

 
class EventUpdate(LoginRequiredMixin,UpdateView):
    model=Event
    fields = [
        'name',
        'address',
        'date'
    ]

class EventDelete(LoginRequiredMixin, DeleteView):
    model=Event
    success_url = '/events/'

class ChildList(LoginRequiredMixin, ListView):
    template_name='main_app/child_list.html'
    def get_queryset(self):
        return Child.objects.filter(user=self.request.user)


class ChildDetail(LoginRequiredMixin, DetailView):
    model = Child

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ChildCreate(LoginRequiredMixin, CreateView):
    model=Child
    fields= [
        'name',
        'date_of_birth',
        'food_allergy'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ChildUpdate(LoginRequiredMixin, UpdateView):
    model=Child
    fields=[
        'name',
        'date_of_birth',
        'food_allergy'
    ]

class ChildDelete(LoginRequiredMixin, DeleteView):
    model=Child
    success_url='/childs/'

@login_required
def assoc_child(request, event_id, child_id):
    Event.objects.get(id=event_id).childs.add(child_id)
    return redirect('events_detail', event_id=event_id)

@login_required
def unassoc_child(request, event_id, child_id):
    Event.objects.get(id=event_id).childs.remove(child_id)
    return redirect('events_detail', event_id=event_id)

    






def signup(request):
    
    error_message = ''
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            user=form.save()
            parent_form=ParentForm()
            user_form=UserForm()
            
            login(request,user)
            return render(request,'parent_form.html',{'parent_form':parent_form,'user_form':user_form,'user':user})
        else:
            error_message='Invalid credentials: Try again'
    form=UserCreationForm()

    
    context={'form': form, 'error_message':error_message}
    return render(request, 'registration/signup.html',context)


def CreateProfile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        parent_form = ParentForm(request.POST, instance=request.user.parent)
        if user_form.is_valid() and parent_form.is_valid():
            user=user_form.save()
            parent_form.save()
            login(request,user)
            return redirect('events_list')
            # messages.success(request, 'Your profile was successfully updated!')
           
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        parent_form = ParentForm(instance=request.user.parent)
    return render(request, 'registration/signup.html', {
        'user_form': user_form,
        'parent_form': parent_form
    })


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


    

