from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('events/', views.EventList.as_view(),name='events_list'),
    path('events/<int:event_id>/',views.events_detail,name='events_detail'),
    path('events/create/', views.EventCreate.as_view(),name='events_create'),
    # associate a toy with a cat (M:M)
    path('events/<int:event_id>/assoc_child/<int:child_id>/', views.assoc_child, name='assoc_child'),
    # unassociate a toy and cat
    path('events/<int:event_id>/unassoc_toy/<int:child_id>/', views.unassoc_child, name='unassoc_child'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup,name='signup' ),
    path('accounts/create_profile', views.CreateProfile,name='create_profile' ),
    path('about/', views.about,name='about'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name = 'events_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name = 'events_delete'),
    path('childs/', views.ChildList.as_view(),name='childs_list'),
    path('childs/<int:pk>/', views.ChildDetail.as_view(),name='childs_detail'),
    path('childs/create/', views.ChildCreate.as_view(),name='childs_create'),
    path('childs/<int:pk>/update/',views.ChildUpdate.as_view(),name='childs_update'),
    path('childs/<int:pk>/delete/', views.ChildDelete.as_view(),name='childs_delete'),
  
]
