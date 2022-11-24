from django.contrib import admin
from .models import Doctor, Patient 


class PatinetInline(admin.TabularInline):
    model = Patient
    extra: 0

class DoctorAdmin(admin.ModelAdmin):
    inlines = [PatinetInline]


# Register your models here.
admin.site.register(Doctor, DoctorAdmin)
