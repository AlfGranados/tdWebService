from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .forms import ProductoForm


class ListaProductos(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def forma_producto(request):
    form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})


@api_view(['POST'])
@parser_classes([JSONParser])
@csrf_exempt
def create_product(request):
    # aquí puedes acceder a los datos del request en formato JSON
    data = request.data
    # crea una nueva instancia del modelo con los datos recibidos
    new_product = Producto(name=data['name'],
                           price=data['price'],
                           description=data['description'])
    # guarda los datos en la base de datos
    new_product.save()

    data = {'mensaje': 'Datos recibidos correctamente'}

    return JsonResponse(data, content_type='application/json')
