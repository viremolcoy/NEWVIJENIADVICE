#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('asesoramientos', views.asesoramientos, name='asesoramientos'),
    path('pagoVijeni', views.pagoVijeni, name='pagoVijeni'),
    path('vijenistore', views.vijeniStore, name='vijenistore'),   
    path('menu', views.menuPrincipal, name='menu'),   
    path('nuevoAsesoramiento', views.nuevoAsesoramiento, name='nuevoAsesoramiento'),   
    path('registro', views.registro, name='registro'),   
    path('inicioSesion', views.iniciosesion, name='inicioSesion'),   
    path('ejercicios', views.ejercicios, name='ejercicios'),  
    path('preguntas', views.preguntas, name='preguntas'),
    path('ayudantia', views.appi, name='appi'),  
]
