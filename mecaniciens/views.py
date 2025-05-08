from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.contrib import messages
from urllib import request
from django.shortcuts import render

from mecaniciens.models import Mecanicien


def liste_rendez_vous():
    return render(request, 'mecanicien/liste_rendez_vous.html')
def mecanicien_dashboard(request):
    return render(request,'mecanicien/dashboard.html')

def liste_reparation():
    return render(request, 'mecanicien/liste_reparation.html')

def deconnexion(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('clients:connexion')
def profil(request, pk):
    mecanicien = get_object_or_404(Mecanicien, pk=pk)
 
    return render(request, 'mecanicien/profil.html', {
        'mecanicien': mecanicien,
        
    })