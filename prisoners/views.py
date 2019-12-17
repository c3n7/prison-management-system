from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Prisoner

class PrisonersListView(ListView):
    model = Prisoner
    ordering = ['id_number', 'first_name', 'last_name']
    template_name = 'prisoners/list.html'

class PrisonersDetailView(DetailView):
    model = Prisoner
    template_name = 'prisoners/detail.html'

class PrisonersUpdateView(UpdateView):
    model = Prisoner
    fields = ('id_number', 'first_name', 'last_name')
    template_name = 'prisoners/edit.html'

class PrisonersCreateView(CreateView):
    model = Prisoner
    fields = ('id_number', 'first_name', 'last_name')
    template_name = 'prisoners/new.html'
