from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Prisoner(models.Model):

    first_name = models.CharField(verbose_name="Firstname", max_length=50)
    second_name = models.CharField(verbose_name="Secondname", max_length=50)
    id_number = models.CharField(verbose_name="Id Number", max_length=50)
    next_kin_name = models.CharField(verbose_name="Name", max_length=50)
    next_kin_id = models.CharField(verbose_name="Id Number", max_length=50)
    next_kin_tel =  models.IntegerField(verbose_name="Phone Number")
    start_date = models.DateField()
    end_date = models.DateField()
    fined_charges = models.IntegerField()
    punishment_status = models.TextField(verbose_name="Status of punishment")


# Create your models here.
