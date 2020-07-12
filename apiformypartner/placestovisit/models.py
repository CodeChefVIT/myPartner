from django.db import models

# Create your models here.
class Add_place(models.Model):
    image= models.ImageField(upload_to='pics')
    name= models.CharField(max_length=80)
    descp= models.TextField()
    distance= models.CharField(max_length=80)
   
