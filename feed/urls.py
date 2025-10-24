
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-feed'), # this will recieve the url after removing everything till localhost:8000/ and check every path if it has nothing this code will execute, if it has about/ the next code will execute and so on.
    path('about/', views.about, name='about-feed'),

]
