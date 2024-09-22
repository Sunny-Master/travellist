from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('destinations/', views.destination_index, name='destination-index')
]