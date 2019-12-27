from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import NextOfKin, KinPrisoner

class NextOfKinDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = NextOfKin
    template_name = 'next_of_kins/detail.html'

    def test_func(self):
        is_kin = NextOfKin.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_kin

class NextOfKinCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = NextOfKin
    fields = ('user',)
    template_name = 'next_of_kins/new.html'

    def test_func(self):
        return self.request.user.is_superuser

class KinPrisonerCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = KinPrisoner
    fields = ('prisoner', 'relationship',)
    template_name = 'kinprisoners/new.html'

    def form_valid(self, form):
        """
        Overridden to always set the kin to the currently
        logged in user
        """
        user = self.request.user
        kin = get_object_or_404(NextOfKin, user=user)
        form.instance.kin = kin
        return super(KinPrisonerCreateView, self).form_valid(form)

    def test_func(self):
        is_kin = NextOfKin.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_kin

class KinPrisonerListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = KinPrisoner
    template_name = 'kinprisoners/list.html'

    def test_func(self):
        is_kin = NextOfKin.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_kin

class KinPrisonerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = KinPrisoner
    template_name = 'kinprisoners/delete.html'
    success_url = reverse_lazy('kinprisoners_list')

    def test_func(self):
        is_kin = NextOfKin.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_kin
