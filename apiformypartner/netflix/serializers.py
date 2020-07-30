from rest_framework import serializers 
from .models import Netflix

class NetflixSerializer(serializers.ModelSerializer):
    class Meta:
        model= Netflix
        fields= '__all__'