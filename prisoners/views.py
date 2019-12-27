from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Prisoner

class PrisonersListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Prisoner
    ordering = ['id_number', 'first_name', 'last_name']
    template_name = 'prisoners/list.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class PrisonersDetailView(LoginRequiredMixin, DetailView):
    model = Prisoner
    template_name = 'prisoners/detail.html'
    login_url = 'login'

class PrisonersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Prisoner
    fields = ('id_number', 'first_name', 'last_name')
    template_name = 'prisoners/edit.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class PrisonersCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Prisoner
    fields = ('id_number', 'first_name', 'last_name')
    template_name = 'prisoners/new.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser
