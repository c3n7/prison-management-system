from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from prisoners.models import Prisoner

class Lawyer(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} <{}>".format(self.user.get_full_name(), self.user.email)

    def get_absolute_url(self):
        return reverse('lawyers_detail', args=[str(self.id)])

class LawyerClient(models.Model):
    lawyer = models.ForeignKey(
        Lawyer,
        on_delete=models.CASCADE
    )
    prisoner = models.ForeignKey(
        Prisoner,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} - {}".format(self.lawyer, self.prisoner)

    def get_absolute_url(self):
        return reverse('lawyers_clients_detail', args=[str(self.id)])
