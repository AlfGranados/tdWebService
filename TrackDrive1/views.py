import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import LocationSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from TrackDrive1.models import Location


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

@csrf_exempt
def location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        point = Location(**data)
        point.save()
        return JsonResponse({'message': 'Punto creado con éxito!'})
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)
