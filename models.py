from django.db import models

class Inventory(models.Model):
    blood_group = models.CharField(max_length=5, unique=True)
    units = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.blood_group} - {self.units}"
# Create your models here.
