import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import LocationSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.shortcuts import render

from .models import Location

def location_list(request):
    locations = Location.objects.all()
    location_data = [
        {
            'latitude': location.latitude,
            'longitude': location.longitude,
            'speed': location.speed,
            'altitude': location.altitude,
            'vsat': location.vsat,
            'usat': location.usat,
            'accuracy': location.accuracy,
            'year': location.year,
            'month': location.month,
            'day': location.day,
            'hour': location.hour,
            'minute': location.minute,
            'second': location.second,
            'uid': location.uid,
        }
        for location in locations
    ]
    return JsonResponse({'locations': location_data})


@csrf_exempt
def location(request):
    if request.method == 'POST':
        point = Location(latitude=request.POST.get('latitude'), longitude=request.POST.get('longitude'),
                         speed=request.POST.get('speed'), altitude=request.POST.get('altitude'),
                         vsat=request.POST.get('vsat'), usat=request.POST.get('usat'),
                         accuracy=request.POST.get('accuracy'), year=request.POST.get('year'),
                         month=request.POST.get('month'), day=request.POST.get('day'),
                         hour=request.POST.get('hour'), minute=request.POST.get('minute'),
                         second=request.POST.get('second'), uid=request.POST.get('uid')
                         )
        point.save()

        return JsonResponse({'message': 'Punto creado con éxito!'})
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)

