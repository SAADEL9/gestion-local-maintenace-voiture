from django.contrib import admin
from .models import Reparation

@admin.register(Reparation)
class ReparationAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'date_debut', 'date_fin', 'etat', 'mecanicien', 'cout')
    search_fields = ('vehicule__marque', 'vehicule__immatricule', 'description')
    list_filter = ('etat', 'date_debut', 'date_fin')
