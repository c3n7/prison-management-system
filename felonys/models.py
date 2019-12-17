from django.db import models
from django.urls import reverse

from prisoners.models import Prisoner

class Felony(models.Model):
    
    prisoner = models.ForeignKey(
        Prisoner,
        on_delete=models.CASCADE,
    )
    title = models.CharField(verbose_name='Title', max_length=50)
    description = models.TextField(verbose_name='Description')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    fine_charged = models.IntegerField(verbose_name='Fine Charged')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('felony_detail', args[str(self.id)])

    class Meta:
        verbose_name = 'Felony'
        verbose_name_plural = 'Felonies'
