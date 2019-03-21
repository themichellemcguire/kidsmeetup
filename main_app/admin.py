from django.contrib import admin
from .models import Event, Child, Parent

# Register your models here.
admin.site.register(Event)
admin.site.register(Child)
admin.site.register(Parent)
