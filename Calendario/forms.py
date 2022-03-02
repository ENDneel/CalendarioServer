from django import forms
from .models import anuncio, calendario
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
class CalendarioForm(forms.ModelForm):

    fecha_i = forms.DateTimeField(
        
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "id": "datetimepicker",
                "placeholder": "Fecha de inicio"
            }
        )
    )
    duracion=forms.IntegerField(
            widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "id": "inputduracion",
                "placeholder": "Duracion"
            }
        ))
    titulo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputTitulo",
                "placeholder": "Titulo"
            }
        ))
    class Meta:
        model = calendario
        fields = '__all__'

class AnuncioForm(forms.ModelForm):
    descripcion = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "name",
                    "placeholder": "Descripcion",
                    "data-sb-validations":"required",
                  
                }
            ))

    imagen = forms.ImageField(required=True,  widget=forms.FileInput(attrs={
         "class":"btn btn-xl",
         "type":"file",
    }))
    
    fecha_publicacion = forms.DateTimeField(
        input_formats=['%Y/%m/%d'],
        widget=forms.DateTimeInput(
            attrs={
                 "class": "form-control",
                "id": "id_fecha_publicacion",
                "placeholder": "Fecha de Publicacion"
            }
        )
    )
    class Meta:
        model = anuncio
        fields = '__all__'



class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')