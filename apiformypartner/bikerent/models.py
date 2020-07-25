from django.db import models

# Create your models here.
class Rent_bike(models.Model):
    name_dealer= models.CharField(max_length=50)
    description= models.TextField()
    address= models.TextField()
    phone_no = models.CharField(max_length=20)