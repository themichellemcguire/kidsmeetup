from django import forms
from .models import Parent, Child, Event
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ('name', 'address', 'phone')

class ChildForm(ModelForm):
    class Meta:
        model = Child
        fields = ('name', 'date_of_birth','description')
