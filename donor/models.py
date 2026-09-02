from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    last_donation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
