from django import forms 
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

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
    
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
        
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
#para usar el cambio de clave en vistas

class PasswordChangingForm(PasswordChangeForm):
    
    old_password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'}))
    new_password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Conform new password'}))
    
    class Meta:
        model = User
        field = ['old_password','new_password1','new_password2']