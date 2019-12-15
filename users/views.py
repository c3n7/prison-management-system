from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AddUserForm

class SignUpView(CreateView):
    form_class = AddUserForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
