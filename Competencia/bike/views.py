from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *

# Create your views here.
def vista_inicio(request):
	return render(request, 'inicio.html')

def vista_listar_corredor(request):
	lista= Corredor.objects.filter()
	return render(request,'listar_corredor.html',locals())

def vista_listar_marca(request):
	listar= Marca.objects.all()
	return render(request,'lista_marca.html',locals())

def vista_listar_categoria(request):
	lista2= Categoria.objects.all()
	return render(request,'lista_categoria.html',locals())

def vista_listar_nacionalidad(request):
	lista= Nacionalidad.objects.filter()
	return render(request,'lista_nacionalidad.html',locals())

def vista_listar_competencia(request):
	listar=Competencia.objects.all()
	return render(request,'lista_competencia.html',locals())

def vista_listar_bicicleta(request):
	lista2= Bicicleta.objects.all()
	return render(request,'listar_bicicleta.html',locals())


def vista_agregar_corredor(request):
	c= Corredor.objects.filter()
	if request.method== 'POST':
		formulary= agregar_corredor_form(request.POST, request.FILES)
		if formulary.is_valid():
			cor= formulary.save(commit= False)
			cor.save()
			formulary.save_m2m()
			return redirect('/lista_corredores/')
	else:
		formulary= agregar_corredor_form()
	return render(request, 'agregar_corredor.html',locals())


def vista_ver_corredor(request, id_cor):
	c= Corredor.objects.get(id= id_cor)
	return render(request, 'ver_corredor.html', locals())

def vista_ver_bicicleta(request, id_bic):
	c= Bicicleta.objects.get(id= id_bic)
	return render(request, 'ver_bicicleta.html', locals())

def vista_editar_corredor(request, id_cor):
	cor= Corredor.objects.get(id= id_cor)
	if request.method== 'POST':
		formulary= agregar_corredor_form(request.POST, request.FILES, instance=cor)
		if formulary.is_valid():
			cor= formulary.save()
			return redirect('/lista_corredores/')
		else:
			formulary= agregar_corredor_form(instance= cor)
	return render(request, 'agregar_corredor.html',locals())

def vista_eliminar_corredor(request, id_cor):
	cor= Corredor.objects.get(id= id_cor)
	cor.delete()
	return redirect('/lista_corredores/')


def vista_editar_bicicleta(request, id_bic):
	bic= Bicicleta.objects.get(id= id_bic)
	if request.method== 'POST':
		formulario= agregar_bicicleta_form(request.POST, request.FILES, instance=bic)
		if formulario.is_valid():
			bic= formulario.save()
			return redirect('/lista_bicicleta/')
		else:
			formulario= agregar_bicicleta_form(instance= bic)
	return render(request, 'agregar_bicicleta.html',locals())

def vista_eliminar_bicicleta(request, id_bic):
	cor= Bicicleta.objects.get(id= id_bic)
	cor.delete()
	return redirect('/lista_bicicleta/')

def vista_agregar_bicicleta(request):
	b= Bicicleta.objects.filter()
	if request.method== 'POST':
		formulario= agregar_bicicleta_form(request.POST, request.FILES)
		if formulario.is_valid():
			bic= formulario.save(commit= False)
			bic.save()
			formulario.save_m2m()
			return redirect('/lista_bicicleta/')
	else:
		formulario= agregar_bicicleta_form()
	return render(request, 'agregar_bicicleta.html',locals())


def vista_login(request):
	usu= ""
	cla= ""
	if request.method=="POST":
		formulario= login_form(request.POST)
		if formulario.is_valid():
			usu= formulario.cleaned_data['usuario']
			cla= formulario.cleaned_data['clave']
			usuario= authenticate(username= usu, password= cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/inicio/')
		else:
			msj="usuario o clave incorrectos"
	formulario= login_form()
	return render(request, 'login.html',locals())

def user_logout(request):
    logout(request)
    return redirect('/login/')


def vista_register(request):
	formulario= register_form()
	if request.method== 'POST':
		formulario= register_form(request.POST)
		if formulario.is_valid():
			usuario= formulario.cleaned_data['username']
			correo= formulario.cleaned_data['email']
			password_1= formulario.cleaned_data['password_1']
			password_2= formulario.cleaned_data['password_2']
			u= User.objects.create_user(username= usuario, email=correo, password= password_1)
			u.save()
			return render(request, 'tanks_for_register.html',locals())
		else:
			return render(request,'register.html', locals())
	return render(request,'register.html',locals())

def ws_corredores_vista(request):
	data= serializers.serialize('json',Corredor.objects.filter())
	return HttpResponse(data, content_type='application/json')

def get_absolute_url(self):
    return reverse('/logout/', args=[str(self.id)])