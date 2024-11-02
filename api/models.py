from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.street + self.city
    