from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# home view
def home(request):
  return render(request, 'home.html')

def destination_index(request):
  destinations = Destination.objects.all()
  return render(request, 'destinations/index.html', { 'destinations': destinations })
