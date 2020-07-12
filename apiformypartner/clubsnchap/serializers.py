from rest_framework import serializers 
from .models import PutClub

class PutClubSerializer(serializers.ModelSerializer):
    class Meta:
        model= PutClub
        fields= '__all__'