from django.shortcuts import render

# Create your views here.

def pagarmercadopago(request):
    context={}
    return render(request, '../client/index.html', context)