from django.contrib import admin
from .models import Reparation

@admin.register(Reparation)
class ReparationAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'client', 'date_debut', 'date_fin', 'etat', 'mecanicien', 'cout')
    list_filter = ('etat', 'mecanicien', 'date_debut')
    search_fields = ('vehicule__immatriculation', 'client__nom', 'description')
    date_hierarchy = 'date_debut'
    readonly_fields = ('date_creation', 'date_modification')



