from rest_framework import serializers
from base.models import Cat

#This converts the data (complex data types :p) from .models into JSON so it can be easily retrieved by the frontend 

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
    
