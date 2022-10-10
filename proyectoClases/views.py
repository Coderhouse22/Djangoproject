from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template 

def hola(request):
    return HttpResponse('Hola clase!</h1>')

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La hora y fecha actual es {fecha_y_hora}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de necimiento es: {fecha}')

def mi_template(request):
    cargar_archivo = open(r'C:\Users\Graciela\Documents\Coderhouse\Proyecto\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)