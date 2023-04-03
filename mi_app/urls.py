from django.urls import path
from mi_app.views import base, inicio, exit, register, editarPerfil, PasswordChangeView, password_change_success, productoList,productoDetalle,productoUpdate,productoDelete,portada
from . import views



urlpatterns = [
    
    path('', base, name="base"),
    path('inicio/', inicio, name="inicio"),
    path('portada/', portada, name="portada"),
    path('logout/', exit, name="exit"),
    path('register/', register, name="register"),
    path('editarperfil/', editarPerfil, name="editarperfil"),
    path('change_password/', PasswordChangeView.as_view(template_name="registration/password_change.html"), name="change-password"),
    path('password_change_success/', password_change_success, name='password_change_success'),
    path("adm", views.AdmProductos.as_view(), name='adm-productos'),
    path("save", views.SaveProducto.as_view(), name='add-producto'),
    path('producto/list', productoList.as_view(), name="List"),
    path(r'^(?P<pk>\d+)$',productoDetalle.as_view(), name="Detail"),
    path(r'^editar/(?P<pk>\d+)$', productoUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', productoDelete.as_view(), name="Delete"),
]