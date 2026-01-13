from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('', include('django.contrib.auth.urls')),
    path('login/', include('django.contrib.auth.urls')),
    path('', lambda request: redirect('event_list')),
    
]