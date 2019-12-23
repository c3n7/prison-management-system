from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Lawyer

class LawyersDetailView(DetailView):
    model = Lawyer
    template_name = 'lawyers/detail.html'

class LawyersCreateView(CreateView):
    model = Lawyer
    fields = ('user',)
    template_name = 'lawyers/new.html'
