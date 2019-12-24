from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Lawyer, LawyerClient

class LawyersDetailView(DetailView):
    model = Lawyer
    template_name = 'lawyers/detail.html'

class LawyersCreateView(CreateView):
    model = Lawyer
    fields = ('user',)
    template_name = 'lawyers/new.html'

class LawyerClientCreateView(CreateView):
    model = LawyerClient
    fields = ('prisoner',)
    template_name = 'lawyerclients/new.html'

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

class LawyerClientListView(ListView):
    model = LawyerClient
    template_name = 'lawyerclients/list.html'

class LawyerClientDeleteView(DeleteView):
    model = LawyerClient
    template_name = 'lawyerclients/delete.html'
    success_url = reverse_lazy('lawyerclients_list')
