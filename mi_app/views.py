from django.shortcuts import render, redirect
from django.http import HttpResponse
#para el login------------------------------------------------------------
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
#para el register------------------------------------------------------------
from .forms import CreacionUsuario


# Create your views here.

#Padre el que hereda------------------------------------------------------------
def base(request):

    return render(request,"mi_app/base.html")

#para el Logout------------------------------------------------------------
def exit(request):

    logout(request)
    return redirect("base")

#para el register------------------------------------------------------------
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

@login_required
def info(request):

    return render(request,"mi_app/info.html")

@login_required
def inicio(request):

    return render(request,"mi_app/inicio.html")

