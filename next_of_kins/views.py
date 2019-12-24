from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import NextOfKin, KinPrisoner

class NextOfKinDetailView(DetailView):
    model = NextOfKin
    template_name = 'next_of_kins/detail.html'

class NextOfKinCreateView(CreateView):
    model = NextOfKin
    fields = ('user',)
    template_name = 'next_of_kins/new.html'

class KinPrisonerCreateView(CreateView):
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

class KinPrisonerListView(ListView):
    model = KinPrisoner
    template_name = 'kinprisoners/list.html'

class KinPrisonerDeleteView(DeleteView):
    model = KinPrisoner
    template_name = 'kinprisoners/delete.html'
    success_url = reverse_lazy('kinprisoners_list')
