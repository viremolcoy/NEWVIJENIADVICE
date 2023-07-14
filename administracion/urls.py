#from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.indexadmin, name='administrador'),
    path('encontrarUsuario/<int:pk>',views.encontrarUsuario,name='encontrarUsuario'),
    path('modificarUsuario',views.modificarUsuario,name='modificarUsuario'),
    path('eliminarUsuario/<str:pk>',views.eliminarUsuario,name='eliminarUsuario'),
    path('agregarUsuario',views.agregarUsuario,name='agregarUsuario'),
    path('loginadmin',views.loginadmin,name='loginadmin'),
    path('accounts/', include('django.contrib.auth.urls')),
]
