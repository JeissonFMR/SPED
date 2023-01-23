from cgitb import text
from django.db import models
from django.db import models
from .clientes import *
from django.contrib.auth.models import User
import datetime
# Create your models here.

class TipoUnidad(models.Model):
    nombre = models.CharField(max_length=150, null=True, unique=True, verbose_name='Tipo de unidad')

    def __str__(self):
        fila =  self.nombre
        return fila
   
class Usuario(models.Model):
    nombre = models.CharField(max_length=150, null=True, unique=True, verbose_name='Usuario que realiza la solicitud')

    def __str__(self):
        fila =  self.nombre
        return fila
    
class Plataforma(models.Model):
    nombre = models.CharField(max_length=150, null=True, unique=True, verbose_name='Plataforma a la cual va dirigida la solicitud:')

    def __str__(self):
        fila =  self.nombre
        return fila
     
class Unidades(models.Model):
    nombre = models.CharField(max_length=150, null=True, verbose_name='Nombre de la unidad')
    def __str__(self):
        fila = self.nombre
        return fila

class ResponsableUnidad(models.Model):
    nombre = models.CharField(max_length=100)
    unidades = models.ForeignKey(Unidades,null=True, blank=True, on_delete=models.PROTECT, verbose_name='Nombre de la unidad')
    def __str__(self):
        fila = self.nombre
        return fila



class Procesos(models.Model):
    # id = models.AutoField(primary_key=True)
    nom_pro = models.CharField(max_length=150, null=True, verbose_name='Nombre del proceso ', unique=True)
    tipoprocesoid = models.ForeignKey(TipoUnidad,null=True, blank=False, on_delete=models.PROTECT, verbose_name='Tipo de unidad que recibe la solicitud')
    plataformaid = models.ForeignKey(Plataforma,null=True, blank=True, on_delete=models.PROTECT, verbose_name='Plataforma a la cual va dirigida la solicitud:')
    usuarioid = models.ForeignKey(Usuario,null=True, blank=True, on_delete=models.PROTECT, verbose_name='Usuario que realiza la solicitud')
    pre_pro = models.CharField(max_length=150, verbose_name='Pregunta base del proceso')
    res_pro = models.CharField(max_length=150, verbose_name='Respuesta base del proceso')
    
    
    doc_pro = models.CharField(max_length=2, choices=suceptible_automatizar, default='No',verbose_name='¿EL proceso requiere documentos para su solución?')
    rep_pro = models.CharField(max_length=150, verbose_name='Persona responsable del proceso')
    tie_pro = models.CharField(max_length=100, verbose_name='Tiempo en resolver la solicitud del usuario')
    tie_sel = models.CharField(max_length=8, choices=horas_proceso, default='Horas', verbose_name='')

    user = models.ForeignKey(User, editable=False, verbose_name='Usuario', on_delete=models.CASCADE, null=True, related_name='Procesos')
    aut_pro = models.CharField(max_length=2, choices=suceptible_automatizar, default='No',verbose_name='Automatizar')

    day  = datetime.datetime.now()
    formatedDay  = day.strftime("%Y/%m/%d")
    formatedHora = day.strftime("%H:%M:%S")
    fec_pro = models.CharField(max_length=50, editable=False, default=formatedDay, verbose_name='Fecha')
    hor_pro = models.CharField(max_length=50, editable=False, default=formatedHora, verbose_name='Hora')

    unidadesid = models.ForeignKey(Unidades,null=True, blank=True, on_delete=models.PROTECT, verbose_name='Unidad que recibe la solicitud')
    responsableid = models.ForeignKey(ResponsableUnidad,null=True, blank=True, on_delete=models.PROTECT, verbose_name='Responsable de la unidad que recibe la solicitud')
    
 
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nom_pro, self.id)
