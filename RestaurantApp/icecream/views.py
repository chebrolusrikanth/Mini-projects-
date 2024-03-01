from django.shortcuts import render
from django.urls import reverse
from .models import icecreams
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Create your views here.

class insert(CreateView):
    model=icecreams
    fields='__all__'
    template_name='icecreamtemps/first.html'
    def get_success_url(self):
        return reverse('icecreaminsert')
    
class selecticecreams(ListView):
    model=icecreams
    fields='__all__'
    template_name='icecreamtemps/select.html'


