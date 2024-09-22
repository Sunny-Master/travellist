from django.shortcuts import render
from .models import Destination
from django.views.generic import ListView, DetailView

# home view
def home(request):
  return render(request, 'home.html')

def destination_index(request):
  destinations = Destination.objects.all()
  return render(request, 'destinations/index.html', { 'destinations': destinations })

class DestinationDetail(DetailView):
  model = Destination
