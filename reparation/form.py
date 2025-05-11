from django import forms
from .models import Reparation

class ReparationForm(forms.ModelForm):
    class Meta:
        model = Reparation
        fields = ['vehicule', 'client', 'date_debut', 'date_fin', 'description', 
                 'etat', 'mecanicien', 'cout', 'notes_mecanicien']
        widgets = {
            'date_debut': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'notes_mecanicien': forms.Textarea(attrs={'rows': 4}),
        }
    
