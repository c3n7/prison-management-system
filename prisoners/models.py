from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Prisoner(models.Model):

    first_name = models.CharField(verbose_name="Firstname", max_length=50)
    last_name = models.CharField(verbose_name="Lastname", max_length=50)
    id_number = models.CharField(verbose_name="Id Number", max_length=50)
    

# Create your models here.
