from django.db import models

# Create your models here.
class Add_place(models.Model):
    image= models.ImageField(upload_to='pics')
    name_of_the_place= models.CharField(max_length=80)
    descp_about_place= models.TextField()
    distance= models.CharField(max_length=80)
   

