from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import * # Importamos el archivo models

# Register your models here.

admin.site.register(ContentType)
admin.site.register(Permission)
admin.site.register(Avatar)