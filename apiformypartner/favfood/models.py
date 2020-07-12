from django.db import models

# Create your models here.
class Rest_favfood(models.Model):
    image= models.ImageField(upload_to='pics')
    name_rest= models.CharField(max_length=80)
    fav_foodname= models.TextField()
    descrip= models.TextField()
    price= models.IntegerField()
    distance= models.CharField(max_length=80)
