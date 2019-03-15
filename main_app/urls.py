from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('events/', views.EventList.as_view(),name='events_list'),


]