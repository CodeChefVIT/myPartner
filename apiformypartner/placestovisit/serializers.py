from rest_framework import serializers 
from .models import Add_place

class AddplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Add_place
        fields= '__all__'