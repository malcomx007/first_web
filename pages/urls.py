

from django import views
from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('index/', views.index , name='index'),
    path('about/', views.about , name='about'),
    path('singup/', views.singup , name='singup'),
    path('', views.singin , name='singin'),
    path('news/', views.news , name='news'),
]
