from django.shortcuts import render, redirect
from django.http import HttpResponse
#para el login------------------------------------------------------------
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):

    return render(request,"mi_app/base.html")

@login_required
def inicio(request):

    return render(request,"mi_app/inicio.html")

def exit(request):

    logout(request)
    return redirect("base")
    