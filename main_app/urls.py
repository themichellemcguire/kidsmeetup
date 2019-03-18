from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('events/', views.EventList.as_view(),name='events_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup,name='signup' ),


]