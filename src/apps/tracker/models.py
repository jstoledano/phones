# coding: utf-8

from django.db import models


class Tracker(models.Model):
    tracker = models.CharField('Folio de Notificación', max_length=13)
    clave_elector = models.CharField(max_length=18)
    folio = models.CharField(max_length=13, primary_key=True)
    paterno = models.CharField(max_length=50)
    materno = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    phone = models.CharField('Teléfono', max_length=10)

    #
    distrito = models.CharField(max_length=2)
    modulo = models.CharField(max_length=6)
    consecutivo = models.CharField(max_length=5)