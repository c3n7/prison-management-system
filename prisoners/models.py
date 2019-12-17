from django.db import models
from django.urls import reverse

class Prisoner(models.Model):

    first_name = models.CharField(verbose_name="Firstname", max_length=50)
    last_name = models.CharField(verbose_name="Lastname", max_length=50)
    id_number = models.CharField(verbose_name="Id Number", max_length=50)

    def __str__(self):
        return str(self.id_number)

    def get_absolute_url(self):
        return reverse('prisoner_detail', args=[str(self.id)])
