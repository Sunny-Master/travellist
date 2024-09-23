from django.shortcuts import render
from .models import Destination
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# home view
def home(request):
  return render(request, 'home.html')

class DestinationList(ListView):
  model = Destination

class DestinationDetail(DetailView):
  model = Destination

class DestinationCreate(CreateView):
  model = Destination
  fields = ['name', 'type', 'city', 'country', 'comment', 'image_url', 'rating']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class DestinationUpdate(UpdateView):
  model = Destination
  fields = ['name', 'type', 'city', 'country', 'comment', 'image_url', 'rating']

class DestinationDelete(DeleteView):
  model = Destination
  success_url = '/destinations/'