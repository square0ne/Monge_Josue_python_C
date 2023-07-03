from django import forms
 #Se importa el modelo de Productos Minimos
from .models import ProductosMinimos

#Se crea el formulario como una clase, con el modelo de Form
class RegistroForm(forms.ModelForm):
    #Se crea la clase meta
    class Meta:
        #Se declara el modelo a usar
        model = ProductosMinimos
        #Se declaran los campos a llenar del formulario
        fields = ['nombre', 'descripcion', 'precio', 'registro', 'estatus']

    def clean(self):

        cleaned_data = super().clean()
        #Se crean las validaciones de cada campo
        nombre = cleaned_data.get('nombre')
        descripcion = cleaned_data.get('descripcion')
        precio = cleaned_data.get('precio')
        registro = cleaned_data.get('registro')
        estatus = cleaned_data.get('estatus')
        #Si uno de los campos no esta lleno
        if (not nombre or not descripcion or not precio
            or not registro or not estatus):
            #Se eleva una excepcion
            raise forms.ValidationError("Todos los campos " +
                                        "deben estar completos")
        return cleaned_data