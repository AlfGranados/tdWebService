from rest_framework import serializers
from .models import Point


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'
