from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Felony(models.Model):
    
    title = models.CharField(verbose_name='Title', max_length=50)
    description = models.TextField(verbose_name='Description')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    fine_charged = models.IntegerField(verbose_name='Fine Charged')
 

# Create your models here.
