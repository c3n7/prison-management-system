from django.contrib import admin
from .models import NextOfKin, KinPrisoner

class NextOfKinAdmin(admin.ModelAdmin):
    model = NextOfKin
    list_display = ['user',]

class KinPrisonerAdmin(admin.ModelAdmin):
    model = KinPrisoner
    list_display = ['kin', 'prisoner',]

admin.site.register(NextOfKin, NextOfKinAdmin)
admin.site.register(KinPrisoner, KinPrisonerAdmin)
