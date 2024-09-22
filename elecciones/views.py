from django.shortcuts import render
from .models import Candidato, Elecciones

l = Elecciones()

def home(request):
    return render(request, 'core/base.html')

def formulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')

        if nombre == '' or apellido == '':
            mensaje = 'Por favor, rellene todos los campos.'
        else:
            c = Candidato(nombre, apellido)
            mensaje = l.inscribir(c)  # Aquí debería devolver el mensaje de éxito o error.
            return render(request, 'core/inscripcion.html', {'mensaje': mensaje})
    
    return render(request, 'core/formulario.html')


def votos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')

        if nombre == '' or apellido == '':
            mensaje = 'Por favor, rellene todos los campos.'
        else:
            mensaje = l.votar(nombre, apellido)
        
        return render(request, 'core/registro.html', {'mensaje': mensaje, 'candidatos': l.candidatos})

    return render(request, 'core/votar.html', {'candidatos': l.candidatos})

def resultados(request):
    resultado = l.resultados()
    
    if isinstance(resultado, Candidato):
        mensaje = f"El candidato con más votos es {resultado.nombre} {resultado.apellido} con {resultado.votos} votos."
    else:
        mensaje = resultado
    
    return render(request, 'core/resultado.html', {'mensaje': mensaje})
