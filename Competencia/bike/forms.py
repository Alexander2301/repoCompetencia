from django import forms
from .models import *
from django.contrib.auth.models import User

class agregar_corredor_form(forms.ModelForm):
	class Meta:
		model= Corredor
		fields= '__all__'

class agregar_bicicleta_form(forms.ModelForm):
	class Meta:
		model= Bicicleta
		fields= '__all__'


class login_form(forms.Form):
	usuario= forms.CharField(widget=forms.TextInput())
	clave= forms.CharField(widget=forms.PasswordInput())

class register_form(forms.Form):
	username = forms.CharField(widget= forms.TextInput())
	email = forms.EmailField(widget= forms.TextInput())	
	password_1  = forms.CharField(label='Password',widget= forms.PasswordInput(render_value= False))
	password_2  = forms.CharField(label='confirmar pasword',widget= forms.PasswordInput(render_value= False))
	
	def clean_username(self):
		username= self.cleaned_data['username']
		try:
			u= User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya registrado')

	def clean_email(self):
		email= self.cleaned_data['email']
		try:
			email= User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Correo Electronico ya registrado')
	
	def clean_password_2(self):
		password_1= self.cleaned_data['password_1']
		password_2= self.cleaned_data['password_2']
		if password_1== password_2:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')