from rest_framework import viewsets
from .serializer import ClientesSerializer
from .models import Clientes
from django.shortcuts import render,redirect

# Create your views here.
class ClientesViewSet(viewsets.ModelViewSet):
    queryset=Clientes.objects.all()
    serializer_class=ClientesSerializer

#Programa: webLink index
def inicio(request):
    return render(request, 'inicio.html')

#Programa: webLink consulta por lista de clientes
def ver_clientes(request): #define funcion DB
    lista_clientes=Clientes.objects.all() #consulta Select from **clientes (segun modelo)
    return render(request, 'clientes.html',{'clientes':lista_clientes}) #carga de datos a plantilla

def registro_cliente(request):
    return render(request, 'registro.html')

#Programa: webLink de registro de nuevo cliente
def reg_clientes(request):
    dni=request.POST['txtdni']
    cliente=request.POST['txtnombre']
    correo=request.POST['txtemail']
    monto=request.POST['txtmonto']
    telefono=request.POST['txttelefono']
    
    cliente_nuevo=Clientes.objects.create(dni_Cliente=dni,nom_Cliente=cliente,email_Cliente=correo,monto_Cliente=monto,tlf_Cliente=telefono)
    return render(request, 'registro.html')

def EliminarCliente(dni_Cliente):
    cliente=Clientes.objects.get(dni_Cliente=dni_Cliente)
    cliente.delete()
    return redirect('/clientes/')


def vEditarCli (request,dni_Cliente):
    cliente=Clientes.objects.get(dni_Cliente=dni_Cliente)
    return render (request, 'editarClientes.html', {'cliente':cliente})

def editarCliente(request):
    
    dni=request.POST['txtdni']
    nombre=request.POST['txtnombre']
    correo=request.POST['txtemail']
    monto=request.POST['txtmonto']
    telefono=request.POST['txttelefono']
    
    cliente=Clientes.objects.get(dni_Cliente=dni)
    cliente.nom_Cliente=nombre
    cliente.email_Cliente=correo
    cliente.monto_Cliente=monto
    cliente.tlf_Cliente=telefono
    cliente.save()
    
    return redirect('/clientes/')

