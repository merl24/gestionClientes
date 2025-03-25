from django.urls import path, include
from rest_framework import routers
from .views import ClientesViewSet
from AppClientes.views import *

ruta=routers.DefaultRouter()
ruta.register('Clientes',ClientesViewSet)

urlpatterns=[
    path('',include(ruta.urls)),
]
