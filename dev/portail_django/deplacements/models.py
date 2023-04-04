from django.contrib.gis.db import models

# Create your models here.

class Lieu(models.Model):
    nom = models.CharField(max_length=100)
    rue = models.CharField(max_length=100)
    no_entree = models.CharField(max_length=10)
    npa = models.IntegerField()
    localite = models.CharField(max_length=50)
    coord = models.PointField()

