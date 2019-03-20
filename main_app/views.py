from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Event
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  UserForm,ParentForm, ChildForm
from django.contrib import messages

# Create your views here.


class EventList(LoginRequiredMixin, ListView):
    model = Event


class EventDetail(LoginRequiredMixin, DetailView):
    model = Event

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

    # success_url='/events/'
    

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
            # return redirect('settings:profile')
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


def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    #instantiate child_form to be rendered in the template
    child_form = ChildForm()
    return render(
        request,
        'main_app/event_detail.html',
        {'event': event, 'child_form': child_form}
    )


def add_child(request, event_id):
    form = ChildForm(request.POST)

    if form.is_valid():
        new_child = form.save(commit=False)
        new_child.event_id = event_id
        new_child.save()
    return redirect('event_detail', event_id=event_id)


    

