from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    user=models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Parent.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.parent.save()

    def __str__(self):
        return self.name
    
    

class Event(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    date=models.DateTimeField()
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('events_list',kwargs={'event_id':self.id})
    
    
    
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
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
    