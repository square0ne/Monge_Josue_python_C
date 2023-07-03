from django.db import models

# Create your models here.
class ProductosMinimos(models.Model):

    #Clase meta
    class Meta:
        verbose_name = "Productos_Minimos"
        verbose_name_plural = "Productos_Minimos"  

    nombre = models.CharField("Nombre", max_length=300, 
                              default="Sin nombrar")
    descripcion = models.CharField("Descripción", max_length=300, 
                              default="Sin especificar")
    precio = models.FloatField("Precio", default=0)
    registro = models.DateField("Fecha de registro", null=False)
    estatus = models.CharField("Estatus", max_length=300, 
                              default="Sin estatus")
    
    def __str__(self):
        return self.nombre
    
    #Regresa una lista con todos los atributos que tiene la clase
    def getAtributos(self):
        return [[self.nombre, "Nombre"], [self.descripcion, "Descripción"],
                [self.precio, "Precio"], 
                [self.registro, "Registro"], 
                [self.estatus, "Estatus"]]