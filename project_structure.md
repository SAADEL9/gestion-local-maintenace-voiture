# Vehicle Maintenance Shop Project Structure

## 1. Django Apps Required
- `clients` - Client management
- `vehiculess` - Vehicle management
- `chatbot` - Chatbot functionality
- `reparation` - Repair management
- `planning` - Appointment scheduling
- `authentication` (Django built-in)

## 2. Database Models

### clients/models.py
```python
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)
    adresse = models.TextField()
    date_inscription = models.DateTimeField(auto_now_add=True)
```

### vehiculess/models.py
```python
class Vehicule(models.Model):
    marque = models.CharField(max_length=100)
    plaque = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)
    derniere_maintenance = models.DateTimeField(null=True, blank=True)
```

### reparation/models.py
```python
class Reparation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    etat = models.CharField(max_length=50)  # En cours, Terminé, En attente
    mecanicien = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cout = models.DecimalField(max_digits=10, decimal_places=2)
```

### planning/models.py
```python
class RendezVous(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_heure = models.DateTimeField()
    status = models.CharField(max_length=50)  # Confirmé, En attente, Annulé
    description = models.TextField()
```

## 3. Views Structure

### Client Views (clients/views.py)
```python
# Authentication
def inscription(request)
def connexion(request)
def deconnexion(request)

# Profile Management
def profil(request)
def modifier_profil(request)

# Vehicle Management
def mes_vehicules(request)
def ajouter_vehicule(request)
def details_vehicule(request, pk)

# Appointments
def prendre_rendez_vous(request)
def mes_rendez_vous(request)
def annuler_rendez_vous(request, pk)
```

### Mechanic Views (reparation/views.py)
```python
def liste_vehicules(request)
def mettre_a_jour_reparation(request, pk)
def consulter_planning(request)
def details_reparation(request, pk)
```

### Admin Views (admin/)
```python
def dashboard(request)
def gerer_clients(request)
def gerer_mecaniciens(request)
def gerer_planning(request)
def gerer_vehicules(request)
```

## 4. URLs Structure

### Main URLs (urls.py)
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clients.urls')),
    path('vehicules/', include('vehiculess.urls')),
    path('reparations/', include('reparation.urls')),
    path('rendez-vous/', include('planning.urls')),
    path('chatbot/', include('chatbot.urls')),
]
```

### Client URLs (clients/urls.py)
```python
urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profil/', views.profil, name='profil'),
    path('profil/modifier/', views.modifier_profil, name='modifier_profil'),
]
```

### Vehicle URLs (vehiculess/urls.py)
```python
urlpatterns = [
    path('mes-vehicules/', views.mes_vehicules, name='mes_vehicules'),
    path('ajouter/', views.ajouter_vehicule, name='ajouter_vehicule'),
    path('<int:pk>/', views.details_vehicule, name='details_vehicule'),
    path('<int:pk>/maintenance/', views.historique_maintenance, name='historique_maintenance'),
]
```

## 5. Templates Structure
```
templates/
├── base.html
├── home.html
├── clients/
│   ├── inscription.html
│   ├── connexion.html
│   ├── profil.html
│   └── modifier_profil.html
├── vehicules/
│   ├── liste.html
│   ├── ajouter.html
│   ├── details.html
│   └── maintenance.html
├── reparations/
│   ├── liste.html
│   ├── details.html
│   └── modifier.html
├── rendez_vous/
│   ├── nouveau.html
│   ├── liste.html
│   └── details.html
└── admin/
    ├── dashboard.html
    ├── clients.html
    ├── mecaniciens.html
    └── planning.html
```

## 6. User Roles and Permissions
- **Client**
  - Create/modify account
  - Register vehicles
  - Book appointments
  - View maintenance history
  - Chat with bot

- **Mécanicien**
  - View assigned vehicles
  - Update repair status
  - View work schedule
  - Access maintenance history

- **Admin**
  - Manage all users
  - Manage mechanics
  - View/modify all appointments
  - Access all vehicle data
  - Generate reports

## 7. Key Features
1. **Authentication System**
   - Registration
   - Login/Logout
   - Password reset

2. **Appointment System**
   - Book appointments
   - Cancel/modify appointments
   - Automatic confirmation

3. **Vehicle Management**
   - Add/modify vehicles
   - Maintenance history
   - Service records

4. **Repair Tracking**
   - Status updates
   - Cost tracking
   - Completion estimates

5. **Planning System**
   - Schedule management
   - Mechanic assignment
   - Availability tracking

6. **Chatbot Integration**
   - FAQ responses
   - Basic support
   - Appointment inquiries

## 8. Security Considerations
1. **Authentication**
   - Secure password storage
   - Session management
   - Password reset security

2. **Authorization**
   - Role-based access
   - Permission checking
   - Secure views

3. **Data Protection**
   - Client data privacy
   - Secure communications
   - Data encryption

4. **Input Validation**
   - Form validation
   - Data sanitization
   - CSRF protection 