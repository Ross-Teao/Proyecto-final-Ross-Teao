from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreacionUsuario(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class editarusuario(UserCreationForm):
    
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email','password1','password2']
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
        # 'first_name','last_name',