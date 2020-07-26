from django.db import models

# Create your models here.
class Netflix(models.Model):
    type_of_plan=models.TextField()
    cost_of_plan=models.IntegerField()
    num_of_people=models.IntegerField()
    avb_status=models.BooleanField(default=True)
    #modify delete personal chatbox
    