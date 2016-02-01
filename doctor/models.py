from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):
	patient_name = models.CharField(max_length=50)
	temp_value = models.FloatField()
	time_recorded = models.DateTimeField()