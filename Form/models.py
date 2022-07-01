
from django.db import models
from django.utils import timezone


class Formulaire(models.Model):
    nom_machine = models.CharField(max_length=20)
    os_version = models.CharField(max_length=10)
    ports_TCP_VPN = models.CharField(max_length=5)
    ports_TCP_Ext = models.CharField(max_length=5)
    ports_UDP_VPN = models.CharField(max_length=5)
    ports_UDP_Ext = models.CharField(max_length=5)
    cores = models.CharField(max_length=2)
    ram = models.CharField(max_length=10)
    alloc_HDD = models.CharField(max_length=10)
    alloc_SSD = models.CharField(max_length=10)
    autre = models.TextField()
    nom_demandeur = models.CharField(max_length=20)
    created_date = models.DateTimeField(
            default=timezone.now)
