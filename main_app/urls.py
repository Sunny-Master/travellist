from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('destinations/', views.destination_index, name='destination-index'),
  path('destinations/<int:pk>/', views.DestinationDetail.as_view(), name='destination-detail'),
  path('destinations/create/', views.DestinationCreate.as_view(), name='destination-create'),
]