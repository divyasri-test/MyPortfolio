from django.urls import path, include
from FirstApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
]
