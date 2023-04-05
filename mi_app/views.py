from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreacionUsuario, UserEditForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from mi_app.models import Avatar,Producto
from django.views import View
from .forms import ProductoForm, ContactForm
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.core.mail import EmailMessage
# Create your views here.

######################################## TEMPLATE PADRE ###############################

def base(request):
    return render(request, "mi_app/portada.html")

######################################## TEMPLATE PORTADA ###############################

def portada(request):
    return render(request, "mi_app/portada.html")

######################################## TEMPLATE INFO CREADOR ###############################

def info_creador(request):
    return render(request, "mi_app/info_creador.html")

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
            return redirect('inicio')
            
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
    

######################################## ENVIAR CORREO ########################################


def contacto_home(request):
    
    return render(request, "mi_app/contacto_home.html")


def contacto_contacto(request):
    
    # print('Tipo de petición: {}'.format(request.method))
    contact_form = ContactForm()
    
    if request.method == 'POST':
        # Estoy enviando el formulario
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            # Enviar el correo electrónico
            email = EmailMessage(
                'Mensaje de contacto recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message),
                email,
                ['b6e5f6c13f8436@inbox.mailtrap.io'],
                reply_to=[email],
            )
            
            try:
                email.send()
                # Está todo OK
                return redirect(reverse('contacto_contacto')+'?ok')
            except:
                # Ha habido un error y retorno a ERROR
                return redirect(reverse('contacto_contacto')+'?error')

    return render(request, 'mi_app/contacto_contacto.html', {'form':contact_form})







email = EmailMessage(
    'Hello',
    'Body goes here',
    'from@example.com',
    ['to1@example.com', 'to2@example.com'],
    ['bcc@example.com'],
    reply_to=['another@example.com'],
    headers={'Message-ID': 'foo'},
)