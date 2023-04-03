from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# avatar

class Avatar(models.Model):
    
    #Vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Subcarpeta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"Usuario: {self.user} - imagen: {self.imagen}"
    
#clase para producto
class Producto(models.Model):
    
    nombre= models.CharField(max_length=100)
    descripcion= models.CharField(max_length=500)
    precio= models.DecimalField(max_digits=100000, decimal_places=0)
    imagen = models.ImageField(upload_to="imagenes", null=True)
    
    def __str__(self):
        return f"{self.nombre} | {self.descripcion} | {self.precio} | {self.imagen}"
    
  
  
