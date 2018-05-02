from django.urls import path, include
from rest_framework import routers 
from bike.models import *
from webservices.views import*

router = routers.DefaultRouter()
router.register(r'corredores', corredor_viewset)
router.register(r'marcas', marca_viewset)
router.register(r'categorias', categoria_viewset)
router.register(r'bicicleta', bicicleta_viewset)
router.register(r'competencia', competencia_viewset)
router.register(r'nacionalidad', nacionalidad_viewset)

urlpatterns = [
		path('api/',include(router.urls),name='vista_api'),
		path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework')),
]