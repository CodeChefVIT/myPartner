from rest_framework import serializers 
from .models import Rent_bike

class RentbikeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rent_bike
        fields= '__all__'