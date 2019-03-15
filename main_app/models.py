from django.db import models

# Create your models here.

class Parent(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Event(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    parent=models.ForeignKey(Parent,on_delete=100)

    def __str__(self):
        return self.name
    
class Child(models.Model):
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)

    def __str__(serlf):
        return self.name

    
