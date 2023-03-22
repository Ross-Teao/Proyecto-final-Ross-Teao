from django.urls import path
from mi_app.views import *

urlpatterns = [
    path('', base, name="base"),
    path('inicio/', inicio, name="inicio"),
    path('logout/', exit, name="exit"),
    path('info/', info, name="info"),
    path('register/', register, name="register"),
    
]