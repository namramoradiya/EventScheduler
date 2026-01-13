from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('new/', views.event_create, name='event_create'),
    path('edit/<int:id>/', views.event_update, name='updating'),
    path('delete/<int:id>/', views.event_delete, name='event_delete'),
    path('register/', views.register, name='register'),
]
