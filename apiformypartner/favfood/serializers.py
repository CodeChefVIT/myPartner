from rest_framework import serializers 
from .models import Rest_favfood

class RestnfoodSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rest_favfood
        fields= '__all__'