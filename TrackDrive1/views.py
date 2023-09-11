import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import LocationSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from django.http import HttpResponse

def mi_vista(request):
    if request.method == 'POST':
        # Obtener los datos del POST
        lat = request.POST.get('lat', '0')
        lon = request.POST.get('lon', '0')

        # Crear una respuesta de texto con la latitud y longitud
        respuesta = f"Latitud: {lat}, Longitud: {lon}"

        # Devolver la respuesta como texto
        return HttpResponse(respuesta, content_type='text/plain')
    else:
        return HttpResponse("Esta vista solo acepta solicitudes POST.", content_type='text/plain')


class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer





