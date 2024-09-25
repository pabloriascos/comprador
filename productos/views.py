from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Categoria, Fuente, Producto, Precio
from .serializers import CategoriaSerializer, FuenteSerializer, ProductoSerializer, PrecioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FuenteViewSet(viewsets.ModelViewSet):
    queryset = Fuente.objects.all()
    serializer_class = FuenteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PrecioViewSet(viewsets.ModelViewSet):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer
