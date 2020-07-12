from django.db import models

# Create your models here.
class PutClub(models.Model):
    logo= models.ImageField(upload_to='pics')
    grp_name= models.CharField(max_length=80)
    descp= models.TextField()
    club= models.BooleanField(default=False)
    chap= models.BooleanField(default=False)
    grptype= models.CharField(max_length=80)