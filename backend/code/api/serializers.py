from rest_framework import serializers
from api.models import Trip, Port

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('id', 'country', 'city', 'name')

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'fromPort', 'toPort', 'cost', 'currency', 
            'departure', 'arrival', 'duration', 'scales', 'sourceURL')