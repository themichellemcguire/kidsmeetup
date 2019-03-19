from django import forms
from .models import Parent
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ('name', 'address', 'phone')
