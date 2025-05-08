from django.urls import path
from . import views
app_name = 'mecaniciens'
urlpatterns = [

    path('dashboard/', views.mecanicien_dashboard, name='mecanicien_dashboard'),
path('profil/<int:pk>/', views.profil, name='profil'),
path('deconnexion/', views.deconnexion, name='deconnexion'),
]