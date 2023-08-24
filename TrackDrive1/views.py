import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import LocationSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Location

class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


@csrf_exempt
class DeviceDataView(APIView):
    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            # Crear una instancia del modelo Location con los datos serializados
            location_instance = Location(
                latitude=serializer.validated_data['latitude'],
                longitude=serializer.validated_data['longitude'],
                altitude=serializer.validated_data['altitude'],
                speed=serializer.validated_data['speed'],
                vsat=serializer.validated_data['vsat'],
                usat=serializer.validated_data['usat'],
                accuracy=serializer.validated_data['accuracy'],
                year=serializer.validated_data['year'],
                month=serializer.validated_data['month'],
                day=serializer.validated_data['day'],
                hour=serializer.validated_data['hour'],
                minute=serializer.validated_data['minute'],
                second=serializer.validated_data['second'],
                uid=serializer.validated_data['uid']
            )
            location_instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


