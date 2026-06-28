from django.urls import path
from . import views
urlpatterns = [
    path('liste',views.listerListe,name="listerListe"),
    path('AjouterListe',views.AjouterListe,name="AjouterListe"),
    path('ModifierListe/<str:pk>',views.ModifierListe,name="ModifierListe"),
    path('client',views.listerClient,name="listerClient"),
    path('ModifierClient/<str:pk>',views.ModifierClient,name="ModifierClient"),
    path('SupprimerListe/<str:pk>',views.SupprimerListe,name="SupprimerListe"),
    path('AjouterClient',views.AjouterClient,name="AjouterClient"),
    path('SupprimerClient/<str:pk>',views.SupprimerClient,name="SupprimerClient"),
    path('register',views.register,name="register"),
    path('connexion',views.connexion,name="connexion"),
    path('deconnexion',views.deconnexion,name="deconnexion"),
    path('home',views.home,name="home"),


 ]
 