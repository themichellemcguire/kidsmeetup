from django.db import models

# Create your models here.

class Parent(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

class Event(models.Model):
    name:models.CharField(max_length=2)
    address:models.CharField(max_length=100)
    parent=models.ForeignKey(Parent,on_delete=100)
    
class Child(models.Model):
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)