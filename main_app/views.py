from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Event
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  UserForm,ParentForm
from django.contrib import messages

# Create your views here.

def home(request):
    return HttpResponse('<h1>Kids Meetup Home</h1>')


class EventList(LoginRequiredMixin, ListView):
    model = Event


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields=['name','address','date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.parent=self.request.user.parent
        return super().form_valid(form)
    success_url='/events/'



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
    # error_message = ''
    

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
