from rest_framework import serializers
from .models import Beverage

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        # Meta data describing the model 

        model = Beverage 
        fields = ['id', 'name', 'description']