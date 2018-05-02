from django.urls import path
from .views import *


urlpatterns = [
	path('inicio/', vista_inicio, name= 'vista_inicio'),
	path('lista_corredores/',vista_listar_corredor, name= 'vista_corredor'),
    path('lista_marca/',vista_listar_marca, name= 'vista_marca'),
    path('lista_competencia/',vista_listar_competencia, name= 'vista_competencia'),
    path('lista_bicicleta/',vista_listar_bicicleta, name= 'vista_bicicleta'),
    path('lista_categoria/',vista_listar_categoria, name= 'vista_categoria'),
    path('lista_nacionalidad/',vista_listar_nacionalidad, name= 'vista_nacionalidad'),
    path('agregar_corredor/',vista_agregar_corredor, name= 'vista_agregar_corredor'),
    path('agregar_bicicleta/',vista_agregar_bicicleta, name= 'vista_agregar_bicicleta'),
    path('ver_corredor/<int:id_cor>/',vista_ver_corredor, name='vista_ver_corredor'),
    path('ver_bicicleta/<int:id_bic>/',vista_ver_bicicleta, name='vista_ver_bicicleta'),
    path('editar_corredor/<int:id_cor>/',vista_editar_corredor, name= 'vista_editar_corredor'),
    path('eliminar_corredor/<int:id_cor>/', vista_eliminar_corredor,name='vista_eliminar_corredor'),
    path('editar_bicicleta/<int:id_bic>/',vista_editar_bicicleta, name= 'vista_editar_bicicleta'),
    path('eliminar_bicicleta/<int:id_bic>/', vista_eliminar_bicicleta,name='vista_eliminar_bicicleta'),
    path('login/',vista_login, name='vista_login'),
    path('logout/',user_logout,name='user_logout'),
    path('register/', vista_register, name='vista_register'),
    path('ws/corredores/',ws_corredores_vista, name='ws_corredores_vista'),
]