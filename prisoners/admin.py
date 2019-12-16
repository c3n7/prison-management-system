from django.contrib import admin
from .models import Prisoner


class PrisonerAdmin(admin.ModelAdmin) :
    model = Prisoner
    list_display = ['first_name','last_name','id_number',]

admin.site.register(Prisoner,PrisonerAdmin)


# Register your models here.
