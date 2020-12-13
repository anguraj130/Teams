from django.contrib import admin
from django.urls import path
from. import views
urlpatterns = [
    path('', views.index, name='index'),
    path('leave', views.leave, name='leave'),
    path('projects', views.projects, name='projects'),
    path('certification', views.certifications, name='certification'),
    path('team', views.team, name='team'),
]