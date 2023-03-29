from django.urls import path
from mi_app.views import base, inicio, exit, info, register, editarPerfil, PasswordChangeView, password_change_success




urlpatterns = [
    
    path('', base, name="base"),
    path('inicio/', inicio, name="inicio"),
    path('logout/', exit, name="exit"),
    path('info/', info, name="info"),
    path('register/', register, name="register"),
    path('editarperfil/', editarPerfil, name="editarperfil"),
    #cambio de clave-------------------------------------
    path('change_password/', PasswordChangeView.as_view(template_name="registration/password_change.html"), name="change-password"),
    path('password_change_success/', password_change_success, name='password_change_success'),

]