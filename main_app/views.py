from django.shortcuts import render
from django.http import HttpResponse

# home view
def home(request):
  return HttpResponse('<h1>Hello Travellers!!</h1>')
