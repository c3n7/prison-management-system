from django.contrib import admin
from .models import Prisoner


class PrisonerAdmin(admin.ModelAdmin) :
    model = Prisoner
    list_display = ['first_name','second_name','id_number','next_kin_name','next_kin_id','next_kin_tel','start_date','end_date','fined_charges','punishment_status',]

admin.site.register(Prisoner,PrisonerAdmin)


# Register your models here.
