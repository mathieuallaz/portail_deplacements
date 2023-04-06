from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lieu(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    utilisateurs = models.ManyToManyField(User, blank=True)   
    rue = models.CharField(max_length=100, blank=True)
    no_entree = models.CharField(max_length=10, blank=True)
    npa = models.IntegerField(null=True, blank=True)
    localite = models.CharField(max_length=50, blank=True)
    coord = models.PointField()

    class Meta:
        verbose_name_plural = 'Lieux'

    def __str__(self):
        return self.nom

class Site(models.Model):
    id_site = models.AutoField(primary_key=True)
    nom_site = models.CharField(max_length=100)
    lieu = models.ForeignKey(Lieu, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom_site

class Societe(models.Model):
    id_societe = models.AutoField(primary_key=True)
    nom_societe = models.CharField(max_length=100)
    sites = models.ManyToManyField(Site, blank=True)

    def __str__(self):
        return self.nom_societe

#class Collaborateur(models.Model):
    #utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    #fonction = 
    #taux =
    #pmr = models.BooleanField()
    #bike_to_work = models.BooleanField()

#class Domicile(models.Model):
    #id_domicile = models.AutoField(primary_key=True)
    #nom_domicile = models.CharField(max_length=100)
    #adresse = models.ForeignKey(Lieu, null=False, on_delete=models.PROTECT)
    #utilisateur = models.ForeignKey(User, on_delete=models.PROTECT)

    #def __str__(self):
        #return self.nom_domicile

class Deplacement(models.Model):
    id_deplacement = models.AutoField(primary_key=True)
    date = models.DateField()
    heure_depart = models.TimeField()
    heure_arrivee = models.TimeField()
    lieu_depart = models.ForeignKey(Lieu, null=False, on_delete=models.PROTECT, related_name ='deplacements_depart')
    lieu_arrivee = models.ForeignKey(Lieu, null=False, on_delete=models.PROTECT, related_name ='deplacements_arrivee')
    utilisateur = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    mode = models.ForeignKey('Mode', null=False, on_delete=models.PROTECT)
    motif = models.ForeignKey('Motif', null=False, on_delete=models.PROTECT)
    raison = models.ForeignKey('Raison', null=False, on_delete=models.PROTECT)

class Mode(models.Model):
    id_mode = models.AutoField(primary_key=True)
    nom_mode = models.CharField(max_length=100)
    alias_mode = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_mode

class Motif(models.Model):
    id_motif = models.AutoField(primary_key=True)
    nom_motif = models.CharField(max_length=100)
    alias_motif = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_motif

class Raison(models.Model):
    id_raison = models.AutoField(primary_key=True)
    nom_raison = models.CharField(max_length=100)
    alias_raison = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_raison