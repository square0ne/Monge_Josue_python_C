from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import ProductosMinimos
from .forms import RegistroForm

class Productos(View):
    #Name of the html page
    template_name = 'productos.html'

    def post(self, request):
        form = RegistroForm(request.POST)    
        if form.is_valid():
            form.save()
            #Se redirije al usuario a la misma pagina
            return redirect('productos')
        return render(request, self.template_name, {'productos': form})
    
    def get(self, request):
        form = ProductosMinimos.objects.all()
        registro = RegistroForm()
        print('Ya inició mi GET -------')
        #Se envia el formulario form
        return render(request, self.template_name, 
                      {'productos': form, 'registro': registro})

class Formulario(View):
    template_name = 'formulario.html'

    def post(self, request):
        form = RegistroForm(request.POST)    
        if form.is_valid():
            form.save()
            #Se redirije al usuario a la misma pagina
            return redirect('productos')
        return render(request, self.template_name, {'form': form})
    
    def get(self, request):
        registro = ProductosMinimos.objects.all()
        #Se envia el formulario form
        return render(request, self.template_name, {'registro': registro})

