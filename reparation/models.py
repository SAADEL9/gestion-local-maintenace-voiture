from django.db import models
from vehicules.models import Vehicule
from django.contrib.auth.models import User

class Reparation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, related_name='reparations')
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    etat = models.CharField(max_length=50)  # En cours, Terminé, En attente
    mecanicien = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reparations')
    cout = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Réparation de {self.vehicule} - {self.etat}"