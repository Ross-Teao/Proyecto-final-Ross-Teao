from django.shortcuts import render, redirect
#para el login-----------------------------------------------------------------
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
#para el register--------------------------------------------------------------
from .forms import CreacionUsuario, UserEditForm, User, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from mi_app.models import Avatar,Producto
from django.core.cache import cache
#ingresar y ver imagen productos
from django.views import View
from .forms import ProductoForm
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
# Create your views here.

######################################## TEMPLATE PADRE ###############################

def base(request):
    return render(request, "mi_app/base.html")

######################################## TEMPLATE PORTADA ###############################

def portada(request):
    return render(request, "mi_app/portada.html")

######################################## TEMPLATE PADRE ###############################

def base(request):
    return render(request, "mi_app/base.html")

######################################## TEMPLATE INICIO ########################################  (use el try-except por un error de "Index Error: list index out of range" y me gusto la solucion que se me ocurrio :D error por usuario sin foto de perfil) 

@login_required
def inicio(request):
    try:
        if request.user.id:
            avatares = Avatar.objects.filter(user=request.user.id).first().imagen.url
            return render(request,("mi_app/inicio.html"), {"url_imagen":avatares } )
        
    except:
            return render(request, "mi_app/inicio.html"  )

######################################## LOGOUT USUARIO ###############################

def exit(request):

    logout(request)
    return redirect("portada")

######################################## REGISTER USUARIO ###############################

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

####################### EDITAR EMAIL-FIRS_NAME-LAST_NAME ##############################


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


######################################## CAMBIO DE CLAVE USUARIO ########################################

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_change_success')
    

def password_change_success(request):
    return render(request,"registration/password_change_success.html")


######################################## CARGAR PRODUCTO,GUARDAR Y MOSTRAR ##############################


class AdmProductos(View):
    
    def get(self, request):
        productos = Producto.objects.all()
        return render(request, "mi_app/adm-productos.html", {
            "productos": productos
        })
        
class SaveProducto(View):
    def get(self, request):
        form = ProductoForm()
        return render(request, "mi_app/add-producto.html", {
            "form": form
        })

    def post(self, request):
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adm-productos'))


######################################## Manejo de producto ver-editar-borrar ########################################

class productoList(ListView):
    
    model = Producto
    template_name = "mi_app/producto_list.html"
    
class productoDetalle(DetailView):
    
    model = Producto
    template_name = "mi_app/producto_detalle.html"

class productoUpdate(UpdateView):
    
    model = Producto
    success_url = "/producto/list"
    fields = ['id','nombre','descripcion','precio']
    
class productoDelete(DeleteView):
    
    model = Producto
    success_url = "/producto/list"
    


