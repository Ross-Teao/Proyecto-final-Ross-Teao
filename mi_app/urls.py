from django.urls import path
from mi_app.views import *
#para el cambio de clave-----------------------------------------
from django.contrib.auth.views import LogoutView,PasswordChangeView


urlpatterns = [
    path('', base, name="base"),
    path('inicio/', inicio, name="inicio"),
    path('logout/', exit, name="exit"),
    path('info/', info, name="info"),
    path('register/', register, name="register"),
    path('editarperfil/', editarPerfil, name="editarperfil"),
    #cambio de clave-------------------------------------
    path('change_password/', PasswordChangeView.as_view(template_name="registration/password_change.html"), name="change-password"),
    # path('password_success/', password_success, name="password_success"),
    path('password-change-success/', password_change_success, name='password_change_success')
    
]