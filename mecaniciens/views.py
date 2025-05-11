from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from mecaniciens.models import Mecanicien
from rendez_vous.models import RendezVous
from reparation.models import Reparation


@login_required
def mecanicien_dashboard(request):
    try:
        mecanicien = request.user.mecanicien
    except Mecanicien.DoesNotExist:
        return redirect('home')

    reparations = Reparation.objects.filter(mecanicien=mecanicien)

    reparations_en_attente = reparations.filter(etat='en_attente').count()
    reparations_en_cours = reparations.filter(etat='en_cours').count()
    reparations_en_pause = reparations.filter(etat='en_pause').count()
    reparations_terminees = reparations.filter(etat='termine').count()
    reparations_annulees = reparations.filter(etat='annule').count()

    reparations_actives = reparations.filter(
        etat__in=['en_attente', 'en_cours', 'en_pause']
    ).order_by('-date_debut')

    date_limite = datetime.now() + timedelta(days=7)
    rendez_vous = RendezVous.objects.filter(
        date_heure__gte=datetime.now(),
        date_heure__lte=date_limite
    ).order_by('date_heure')

    context = {
        'reparations_en_attente': reparations_en_attente,
        'reparations_en_cours': reparations_en_cours,
        'reparations_en_pause': reparations_en_pause,
        'reparations_terminees': reparations_terminees,
        'reparations_annulees': reparations_annulees,
        'reparations_actives': reparations_actives,
        'rendez_vous': rendez_vous,
    }

    return render(request, 'mecanicien/dashboard.html', context)


def liste_rendez_vous(request):
    return render(request, 'mecanicien/liste_rendez_vous.html')


def liste_reparation(request):
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
