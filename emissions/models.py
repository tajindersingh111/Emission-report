from django.db import models

# Create your models here.

# emissions/models.py

from django.db import models

class VehicleInfo(models.Model):
    vin = models.CharField(max_length=17, primary_key=True)
    company_name = models.CharField(max_length=255)
    vehicle_date = models.DateField()

    def __str__(self):
        return self.vin

class EmissionsData(models.Model):
    vin = models.ForeignKey(VehicleInfo, on_delete=models.CASCADE)
    route_id = models.CharField(max_length=255)
    ref_no = models.CharField(max_length=255)
    emission_date = models.DateField()
    co2_emissions = models.FloatField()
    nox_emissions = models.FloatField()

    def __str__(self):
        return f"{self.vin} - {self.emission_date}"
