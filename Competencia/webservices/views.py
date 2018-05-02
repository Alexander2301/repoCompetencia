from bike.models import *
from .serializer import *
from rest_framework import viewsets

class corredor_viewset(viewsets.ModelViewSet):
	queryset = Corredor.objects.all()
	serializer_class = corredor_serializer

class marca_viewset(viewsets.ModelViewSet):
	queryset = Marca.objects.all()
	serializer_class = marca_serializer


class categoria_viewset(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = categoria_serializer

class bicicleta_viewset(viewsets.ModelViewSet):
	queryset = Bicicleta.objects.all()
	serializer_class = bicicleta_serializer

class nacionalidad_viewset(viewsets.ModelViewSet):
	queryset = Nacionalidad.objects.all()
	serializer_class = nacionalidad_serializer


class competencia_viewset(viewsets.ModelViewSet):
	queryset = Competencia.objects.all()
	serializer_class = competencia_serializer

