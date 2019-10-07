from django.db import models
from django.conf import settings


class Drug(models.Model):
    is_opioid = models.IntegerField()
    name = models.TextField()

class Prescriber(models.Model):
    prescriber_id = models.BigIntegerField()
    gender = models.TextField()
    crendentials = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    specialty = models.TextField()
    state = models.TextField()
    is_opioid_prescriber = models.IntegerField()

class DrugPrescriber(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    prescriber = models.ForeignKey(Prescriber, on_delete=models.CASCADE)
    quantity_prescribed = models.IntegerField()