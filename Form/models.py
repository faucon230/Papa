
from django.db import models
from django.utils import timezone
from django import forms


class Formulaire(models.Model):
    nom_demandeur = models.CharField(max_length=20,default='nom')
    prenom_demandeur = models.CharField(max_length=20,default='prénom')
    mail = models.CharField(max_length=40,default='exemple@mail.com')

    nom_de_la_machine = models.CharField(max_length=20)
    url = models.CharField(max_length=20,default = 'sandbox.ensea.fr')
    version_OS = models.CharField(max_length=21,default = 1, choices = (('container debian 10.7', 'Container debian 10.7'),('container debian 11.0','Container debian 11.0'),('VM','VM') ))

    vpn = models.CharField(max_length=3, choices = (('oui', 'Oui'),('non', 'Non')))
    ports_TCP_Ext = models.CharField(max_length=5)
    ports_UDP_Ext = models.CharField(max_length=5)
    nombre_de_coeurs = models.IntegerField(default = 1, choices = ((1, '1'),(2,'2'),(3,'3'),(4,'4')) )
    ram = models.IntegerField()

    alloc_HDD = models.CharField(max_length=10)
    alloc_SSD = models.CharField(max_length=10)

    autre =  models.CharField(max_length=100)
    utilisation =  models.CharField(max_length=100, null=True, blank=True)

    date_debut2 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    date_début = models.DateField(default=timezone.now)
    date_fin = models.DateField(default=timezone.now)
    date_destruction = models.DateField(default=timezone.now)

    etat = models.CharField(max_length=40,default = 0 , choices = (('En fonctionnement', 'En fonctionnement'),('En arrêt','En arrêt'),('Détruite','Détruite'),('A créer','A créer')) )
    date_de_demande = models.DateField(default=timezone.now)



