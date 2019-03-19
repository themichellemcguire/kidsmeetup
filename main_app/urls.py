from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('events/', views.EventList.as_view(),name='events_list'),
    path('events/<int:pk'/,views.EventDetail)
    path('events/create', views.EventCreate.as_view(),name='events_create'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup,name='signup' ),
    path('accounts/create_profile', views.CreateProfile,name='create_profile' ),



]