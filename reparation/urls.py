from django.urls import path
from . import views

app_name = 'reparation'

urlpatterns = [
    path('', views.liste_reparations, name='liste_reparations'),
   
    path('<int:pk>/', views.detail_reparation, name='detail_reparation'),
    path('<int:pk>/modifier/', views.modifier_reparation, name='modifier_reparation'),
    path('<int:pk>/supprimer/', views.supprimer_reparation, name='supprimer_reparation'),
]
