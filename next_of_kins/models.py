from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from prisoners.models import Prisoner

class NextOfKin(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} <{}>".format(self.user.get_full_name(), self.user.email)

    def get_absolute_url(self):
        return reverse('nextofkin_detail', args=[str(self.id)])

class KinPrisoner(models.Model):
    kin = models.ForeignKey(
        NextOfKin,
        on_delete=models.CASCADE
    )
    prisoner = models.ForeignKey(
        Prisoner,
        on_delete=models.CASCADE
    )
    relationship = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.kin, self.prisoner)

    def get_absolute_url(self):
        return reverse('kinprisoners_list')

