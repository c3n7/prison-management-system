from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

class PrisonersAdminListView(ListView) :
    model =  models.Prisoner
    template_name = 'prisoners_admin_list.html'
class PrisonersAdminDetailView(DetailView) :
    model =  models.Prisoner
    template_name = 'prisoners_admin_detail.html'   
class PrisonersAdminUpdateView(UpdateView) :
    model =  models.Prisoner
    fields ['title','summary',]
    template_name = 'prisoners_admin_edit.html'
class PrisonersAdminCreateView(CreateView) :
    model =  models.Prisoner
    template_name = 'prisoners_admin_new.html' 
    fields = ['title','code','summary']   
# Create your views here.
