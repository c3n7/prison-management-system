from django.contrib import admin
from .models import Lawyer, LawyerClient

class LawyerAdmin(admin.ModelAdmin):
    model = Lawyer
    list_display = ['user',]

class LawyerClientAdmin(admin.ModelAdmin):
    model = Lawyer
    list_display = ['lawyer', 'prisoner',]

admin.site.register(Lawyer, LawyerAdmin)
admin.site.register(LawyerClient, LawyerClientAdmin)
