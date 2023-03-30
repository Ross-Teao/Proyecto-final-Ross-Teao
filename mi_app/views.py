from django.shortcuts import render, redirect
from django.http import HttpResponse
#para el login-----------------------------------------------------------------
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
#para el register--------------------------------------------------------------
from .forms import CreacionUsuario, UserEditForm, User, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import Avatar

 
# Create your views here.

# Template Padre------------------------------------------------------------

# def base(request):
#     return render(request, "mi_app/base.html"  )

@login_required
def base(request):
    if request.user.id:
        avatares = Avatar.objects.filter(user=request.user.id)[0].imagen.url
        return render(request,("mi_app/base.html"), {"url_imagen":avatares } )
    
    else:
            return render(request,"mi_app/base.html")

# Logout usuario-----------------------------------------------------------------
def exit(request):

    logout(request)
    return redirect("inicio")

# Register usuario---------------------------------------------------------------
def register(request):
    data={
        'form':CreacionUsuario()
    }
    if request.method == 'POST':
        user_creation_form= CreacionUsuario(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username= user_creation_form.cleaned_data['username'], password= user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('base')
            
    return render(request,"registration/register.html", data)

# Editar perfil usuarios-------------------------------------------------------

@login_required
def editarPerfil(request):
    

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()
            
            return render(request, "mi_app/inicio.html")

    else:      
        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "mi_app/editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})


# Cambio de clave usuario-----------------------------------------------------------------

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_change_success')
    

def password_change_success(request):
    return render(request,"registration/password_change_success.html")


# Vistas para trabajar------------------------------------------------------------

@login_required
def info(request):

    return render(request,"mi_app/info.html")

@login_required
def inicio(request):
    
    return render(request, "mi_app/inicio.html")

# @login_required
# def inicio(request):
#     if request.user.id:
#         avatares = Avatar.objects.filter(user=request.user.id)[0].imagen.url
#         return render(request,("mi_app/inicio.html"), {"url_imagen":avatares } )
    
#     else:
#             return render(request, "mi_app/inicio.html"  )


