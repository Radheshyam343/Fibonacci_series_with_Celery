from . import views
from django.urls import path

urlpatterns = [
    path('fibonacci/', views.fibonacci, name='fibonacci'),
    
]