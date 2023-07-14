from django.shortcuts import render

# Create your views here.

def inicio(request):
    context={}
    return render(request, 'index.html', context)

def asesoramientos(request):
    context={}
    return render(request, 'asesoramientos.html', context)

def pagoVijeni(request):
    context={}
    return render(request, 'pagarase.html', context)

def vijeniStore(request):
    context={}
    return render(request, 'storenew.html', context)

def menuPrincipal(request):
    context={}
    return render(request, 'menuprincipal.html', context)

def nuevoAsesoramiento(request):
    context={}
    return render(request, 'nuevoasesoramiento.html', context)

def registro(request):
    context={}
    return render(request, 'registro.html', context)


def iniciosesion(request):
    context={}
    return render(request, 'iniciosesion.html', context)

def ejercicios(request):
    context={}
    return render(request, 'ejercicios.html', context)

def preguntas(request):
    context={}
    return render(request, 'preguntas.html', context)

def appi(request):
    context={}
    return render(request, 'apichatgpt.html', context)

