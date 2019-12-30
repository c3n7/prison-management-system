from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Lawyer, LawyerClient

class LawyersDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Lawyer
    template_name = 'lawyers/detail.html'
    login_url = 'login'

    def test_func(self):
        is_lawyer = Lawyer.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_lawyer

class LawyersCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Lawyer
    fields = ('user',)
    template_name = 'lawyers/new.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class LawyerClientCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = LawyerClient
    fields = ('prisoner',)
    template_name = 'lawyerclients/new.html'
    login_url = 'login'

    # def get_initial(self):
        # initial = super(LawyerClientCreateView, self).get_initial()
        # user = self.request.user
        # lawyer = get_object_or_404(Lawyer, user=user)
        # initial['lawyer'] = lawyer
        # return initial

    def form_valid(self, form):
        """
        Overridden to always set the lawyer to the currently
        logged in user
        """
        user = self.request.user
        lawyer = get_object_or_404(Lawyer, user=user)
        form.instance.lawyer = lawyer
        return super(LawyerClientCreateView, self).form_valid(form)

    def test_func(self):
        is_lawyer = Lawyer.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_lawyer

class LawyerClientListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = LawyerClient
    template_name = 'lawyerclients/list.html'
    login_url = 'login'

    def test_func(self):
        is_lawyer = Lawyer.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_lawyer

    def get_queryset(self):
        """
        Return only the clients for the current lawyer
        """
        lawyer = Lawyer.objects.filter(user=self.request.user).first()
        return LawyerClient.objects.filter(
            lawyer=lawyer)

class LawyerClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LawyerClient
    template_name = 'lawyerclients/delete.html'
    success_url = reverse_lazy('lawyerclients_list')
    login_url = 'login'

    def test_func(self):
        is_lawyer = Lawyer.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_lawyer
