from django.db import models

# Create your models here.

class Clientes(models.Model):
    dni_Cliente=models.CharField(max_length=8, unique=True)
    nom_Cliente=models.CharField(max_length=25)
    email_Cliente=models.EmailField()
    monto_Cliente=models.DecimalField(max_digits=8,decimal_places=4)
    tlf_Cliente=models.CharField(max_length=9)
