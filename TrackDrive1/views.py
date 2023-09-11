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
from django.http import HttpResponse

def mi_vista(request):
    # Obtener el dato de la solicitud (por ejemplo, a través de la URL)
    dato = request.GET.get('dato', '')

    # Crear un mensaje de texto
    mensaje = f"Recibido el dato: {dato}"

    # Devolver la respuesta como texto
    return HttpResponse(mensaje, content_type='text/plain')

class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer





