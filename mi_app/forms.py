from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Producto

class CreacionUsuario(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserEditForm(UserCreationForm):
    #Para quitar el apartado de claves debido a que no los quiero en esta parte------------------------------------------
    def __init__(self, *args, **Kwargs):
        
        super(UserEditForm,self).__init__(*args, **Kwargs)
        del self.fields ['password1']
        del self.fields ['password2']
    
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}),  max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),  max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),  max_length=50)
        
    class Meta:
        model = User
        fields = ['email','first_name','last_name']
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
#para usar el cambio de clave en vistas

class PasswordChangingForm(PasswordChangeForm):
    
    old_password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'}))
    new_password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}))
    
    class Meta:
        model = User
        field = ['old_password','new_password1','new_password2']

#clase para productos       
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['id','nombre','descripcion','precio','imagen']
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),  max_length=50)
    descripcion = forms.CharField (widget=forms.Textarea(attrs={"class":"form-control"}), max_length=100)
    precio = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control"}), max_digits=7, decimal_places=2)
    imagen = forms.ImageField(label="Avatar", required=False, widget=forms.FileInput(attrs={'class':'form-control'}))
    
class ProductoFormulario(forms.Form):
    
    nombre= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),  max_length=50)
    descripcion= forms.CharField (widget=forms.Textarea(attrs={"class":"form-control"}), max_length=100)
    precio= forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control"}), max_digits=7, decimal_places=2)
    
    
#mensaje --------------------------------------------------------------------------------
    
class ContactForm(forms.Form):
    
    name = forms.CharField(label='Nombre y Apellido', required=True, min_length=5, max_length=25, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduzca sus datos'}))

    email = forms.EmailField(label='Correo Electrónico', required=True, max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Introduzca su email'}))

    message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escriba aquí su mensaje...','rows':5}))