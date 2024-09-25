from rest_framework import serializers
from .models import Categoria, Fuente, Producto, Precio

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class FuenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuente
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    
    class Meta:
        model = Producto
        fields = '__all__'

class PrecioSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    fuente = FuenteSerializer()
    
    class Meta:
        model = Precio
        fields = '__all__'
