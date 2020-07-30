from django.db import models

# Create your models here.
class Rest_favfood(models.Model):
    image= models.ImageField(upload_to='pics')
    name_of_rest= models.CharField(max_length=80)
    fav_foodname= models.TextField()
    description= models.TextField()
    price_food= models.IntegerField()
    distance= models.CharField(max_length=80)
