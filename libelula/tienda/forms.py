from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usuario",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Ingrese un nombre de producto','class':'form-control'}))
    categoria =forms.ModelChoiceField(label="",queryset=Categoria.objects.all(),empty_label="Seleccionar una categoria",widget=forms.Select(attrs={'class': 'form-control'})) #forms.CharField(label="Categoria")
    precio = forms.FloatField(label="",min_value=0.00,widget=forms.NumberInput(attrs={'placeholder':'Ingrese el Precio','class':'form-control'}))
    cantidad_disponible = forms.FloatField(label="", min_value=0,widget=forms.NumberInput(attrs={'placeholder':'Ingrese la cantidad','class':'form-control'}))
    descripcion = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Ingrese una descripción','class':'form-control'}))
    imagen = forms.FileField(label="",widget=forms.FileInput(attrs={'placeholder':'Ingrese una imágen','class':'form-control'}))
    
    class Meta:
        model = Producto
        fields = ['nombre','categoria','precio','cantidad_disponible',
        'descripcion','imagen']

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Ingrese un nombre de categoria','class':'form-control'}))
    descripcion = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Ingrese una descripción','class':'form-control'}))
    class Meta:
        model = Producto
        fields = ['nombre','descripcion']
       
class BusquedaForm(forms.Form):
    terminos_busqueda = forms.CharField(max_length=100, required=False, label='Buscar producto')        