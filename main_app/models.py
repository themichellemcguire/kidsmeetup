from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

ALLERGY_FOODS = (
    ('M', 'Milk'),
    ('E','Eggs'),
    ('P','Peanuts'),
    # ('T','Tree nuts'),
    # ('S' 'Soy'),
    # ('W','Wheat'),
    # ('F','Fish'),
    # ('L','Shellfish')
)
    

class Parent(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    

    def __str__(self):
        return self.name

class Event(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    # date=models.DateTimeField()
    parent=models.ForeignKey(Parent,on_delete=100)

    def __str__(self):
        return self.name
    
    
    
class Child(models.Model):
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    food_allergy=models.CharField(
        max_length=1,
        choices=ALLERGY_FOODS,
        default=ALLERGY_FOODS[0][0]
    )
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
    
