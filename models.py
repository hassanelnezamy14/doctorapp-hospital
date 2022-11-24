from django.db import models

# Create your models here.
class Doctor(models.Model):
    Doctor_name = models.CharField(max_length=30)
    registratio_data = models.DateTimeField("data registered")

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    registration_data = models.DateTimeField("data registered")
    waititng_status = models.BooleanField()


    @property
    def is_waiting(self):
        return bool(self.waititng_status)