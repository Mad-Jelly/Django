from django.db import models

# Create your models here.
class pm_collect(models.Model):
    pm_value=models.FloatField(max_length=5)
    pm_date=models.DateTimeField()
