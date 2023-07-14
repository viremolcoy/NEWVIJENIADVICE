from pyexpat.errors import messages
from django.shortcuts import redirect, render
from vijeniadviceweb.models import Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def indexadmin(request):
    usuarios = Usuario.objects.all()
    context={'usuarios':usuarios}
    return render(request, '../templates/indexadmin.html', context)

def loginadmin(request):
    context={}
    return render(request, 'loginadmin.html', context)

def agregarUsuario(request):
        if request.method != "POST":
            usu=Usuario.objects.all();
            context={'usu':usu}
            return render(request,'../templates/agregarUsuario.html',context)
        else:
            #Es un POST,por lo tanto se recuperan los datos del formulario
            nombre=request.POST["usuario"]
            contra=request.POST["contra"]

            
            obj=Usuario.objects.create(
                                    usuario=nombre,
                                    contraseña=contra)
            obj.save()
            context={'mensaje':'OK, datos guardados con éxito'}
            return render(request,'../templates/agregarUsuario.html',context)

    
def encontrarUsuario(request, pk):
    usuario = Usuario.objects.get(id_usuario=pk)
    if usuario:
        context = {'usuario': usuario}
        return render(request, '../templates/modificarUsuario.html', context)
    else:
        context = {'mensaje': 'Error, id usuario no existe'}
        return render(request, '../templates/indexadmin.html', context)


def modificarUsuario(request):
    if request.method == 'POST':
        idUsuario = request.POST["idUsuario"]
        n_usuario = request.POST["nombreUsuario"]
        contra = request.POST["contraseña"]

        usuario = Usuario.objects.get(id_usuario=idUsuario)
        usuario.usuario = n_usuario
        usuario.contraseña = contra
        usuario.save()

        return redirect('administrador')  # Redirige al usuario a la vista 'administrador'
    else:
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios}
        return render(request, '../templates/indexadmin.html', context)


def eliminarUsuario(request,pk):
    context={}
    try:
        usuario=Usuario.objects.get(id_usuario=pk)
        usuario.delete()
        usuario="Ok, Datos eliminados satisfactoriamente"
        usuarios=Usuario.objects.all()
        context={'usuarios':usuarios,'mensaje':mensaje}
        return render(request,'../templates/indexadmin.html',context)
    except:
        mensaje="Error, id usuario no existe"
        usuarios=Usuario.objects.all()
        context={'usuarios':usuarios,'mensaje':mensaje}
        return render(request,'../templates/indexadmin.html',context)

