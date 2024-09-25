from django.urls import path, include
from rest_framework import routers
from .views import CategoriaViewSet, FuenteViewSet, ProductoViewSet, PrecioViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'fuentes', FuenteViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'precios', PrecioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
