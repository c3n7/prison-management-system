from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import NextOfKin

class NextOfKinDetailView(DetailView):
    model = NextOfKin
    template_name = 'next_of_kins/detail.html'

class NextOfKinCreateView(CreateView):
    model = NextOfKin
    fields = ('user',)
    template_name = 'next_of_kins/new.html'
