from django.contrib import admin
from .models import Felony

class FelonyAdmin(admin.ModelAdmin) :
    model = Felony
    list_display = ['title','description','start_date','end_date','fine_charged',]

admin.site.register(Felony, FelonyAdmin)


# Register your models here.
