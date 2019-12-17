from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Felony
from prisoners.models import Prisoner

class FelonysListView(ListView):
    model = Felony
    ordering = ['prisoner', 'title']
    template_name = 'felonys/list.html'

class FelonysDetailView(DetailView):
    model = Felony
    template_name = 'felonys/detail.html'

class FelonysUpdateView(UpdateView):
    model = Felony
    fields = ('title', 'description', 'start_date', 'end_date', 'fine_charged')
    template_name = 'felonys/edit.html'

class FelonysCreateView(CreateView):
    model = Felony
    fields = ('prisoner', 'title', 'description', 'start_date', 'end_date', 'fine_charged')
    template_name = 'felonys/new.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden to ensure that the passed primary key does exist
        """
        self.prisoner = get_object_or_404(Prisoner, pk=kwargs['prisoner_pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view
        """
        initial = super(FelonysCreateView, self).get_initial()
        initial['prisoner'] = self.prisoner
        return initial
