from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import pizza
from django.views.generic.list import ListView
# Create your views here.


class insertpizza(CreateView):
    model=pizza
    fields='__all__'
    template_name='icecreamtemps/first.html'
    def get_success_url(self):
        return reverse('insertpizzaurl')
    

class selectpizza(ListView):
    model=pizza
    fields='__all__'
    template_name='icecreamtemps/display.html' 
