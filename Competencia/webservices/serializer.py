from rest_framework import serializers
from bike.models import *

class corredor_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Corredor
		fields = ('url', 'nombre','edad','categoria','nacionalidad','bicicleta','competencia','foto')

class marca_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Marca 
		fields = ('url', 'nombre')


class categoria_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Categoria 
		fields = ('url', 'nombre')

class competencia_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Competencia
		fields = ('url', 'nombre')


class bicicleta_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Bicicleta
		fields = ('url', 'serie','color','marca')

class nacionalidad_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Nacionalidad 
		fields = ('url', 'nombre')
