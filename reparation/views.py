from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reparation
from .form import ReparationForm
from vehicules.models import Vehicule
from clients.models import Client
from mecaniciens.models import Mecanicien

@login_required
def liste_reparations(request):
    try:
        # Essayer de récupérer le mécanicien connecté
        mecanicien = Mecanicien.objects.get(user=request.user)
        # Si c'est un mécanicien, montrer ses réparations assignées
        reparations = Reparation.objects.filter(mecanicien=mecanicien).order_by('-date_creation')
        user_type = 'mecanicien'
    except Mecanicien.DoesNotExist:
        try:
            # Si ce n'est pas un mécanicien, essayer de récupérer le client
            client = Client.objects.get(user=request.user)
            # Si c'est un client, montrer ses réparations
            reparations = Reparation.objects.filter(client=client).order_by('-date_creation')
            user_type = 'client'
        except Client.DoesNotExist:
            messages.error(request, "Vous n'avez pas les permissions nécessaires.")
            return redirect('home')
    
    return render(request, 'reparation/liste_reparations.html', {
        'reparations': reparations,
        'user_type': user_type
    })

@login_required
def detail_reparation(request, pk):
    reparation = get_object_or_404(Reparation, pk=pk)
    
    # Vérifier les permissions
    try:
        mecanicien = Mecanicien.objects.get(user=request.user)
        if reparation.mecanicien != mecanicien:
            messages.error(request, "Vous n'avez pas accès à cette réparation.")
            return redirect('reparation:liste_reparations')
        user_type = 'mecanicien'
    except Mecanicien.DoesNotExist:
        try:
            client = Client.objects.get(user=request.user)
            if reparation.client != client:
                messages.error(request, "Vous n'avez pas accès à cette réparation.")
                return redirect('reparation:liste_reparations')
            user_type = 'client'
        except Client.DoesNotExist:
            messages.error(request, "Vous n'avez pas les permissions nécessaires.")
            return redirect('home')
    
    return render(request, 'reparation/detail_reparation.html', {
        'reparation': reparation,
        'user_type': user_type
    })

@login_required
def modifier_reparation(request, pk):
    reparation = get_object_or_404(Reparation, pk=pk)
    
    # Vérifier si c'est un mécanicien
    try:
        mecanicien = Mecanicien.objects.get(user=request.user)
        if reparation.mecanicien != mecanicien:
            messages.error(request, "Vous n'avez pas accès à cette réparation.")
            return redirect('reparation:liste_reparations')
    except Mecanicien.DoesNotExist:
        messages.error(request, "Seuls les mécaniciens peuvent modifier les réparations.")
        return redirect('reparation:liste_reparations')
    
    if request.method == 'POST':
        form = ReparationForm(request.POST, instance=reparation)
        if form.is_valid():
            reparation = form.save()
            messages.success(request, 'Réparation modifiée avec succès.')
            return redirect('reparation:detail_reparation', pk=reparation.pk)
    else:
        form = ReparationForm(instance=reparation)
    return render(request, 'reparation/modifier_reparation.html', {'form': form, 'reparation': reparation})

@login_required
def supprimer_reparation(request, pk):
    reparation = get_object_or_404(Reparation, pk=pk)
    
    # Vérifier si c'est un mécanicien
    try:
        mecanicien = Mecanicien.objects.get(user=request.user)
        if reparation.mecanicien != mecanicien:
            messages.error(request, "Vous n'avez pas accès à cette réparation.")
            return redirect('reparation:liste_reparations')
    except Mecanicien.DoesNotExist:
        messages.error(request, "Seuls les mécaniciens peuvent supprimer les réparations.")
        return redirect('reparation:liste_reparations')
    
    if request.method == 'POST':
        reparation.delete()
        messages.success(request, 'Réparation supprimée avec succès.')
        return redirect('reparation:liste_reparations')
    return render(request, 'reparation/supprimer_reparation.html', {'reparation': reparation})
