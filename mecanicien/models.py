from django.db import models
class Mecanicien(models.Model):
    nom = models.CharField(max_length=10)
    prenom = models.CharField(max_length=10)
    experience = models.IntegerField()
    specialite = models.CharField(max_length=10)
    