# pages/urls.py
from django.urls import path
from pages import views
from django.contrib import admin
from .views import record_time_spent


urlpatterns = [
    path('record_time_spent/', record_time_spent, name='record_time_spent'),
    path("home/", views.home, name='home'),
    path("login/", views.LoginPageView, name='login'),
    path("BigJohn/", views.BigJohn, name='BigJohn'),
    path("ArtSmart/", views.ArtSmart, name='ArtSmart'),
    path("CentralBank/", views.CentralBank, name='CentralBank'),
    path("EngineersWorkshop/", views.Engineer, name='EngineersWorkshop'),
    path("Farm/", views.Farm, name='Farm'),
    path("Firehouse/", views.Firehouse, name='Firehouse'),
    path("Forts/", views.Forts, name='Forts'),
    path("Hospital/", views.Hospital, name='Hosptial'),
    path("IceCream/", views.IceCream, name='IceCream'),
    path("KidsPort/", views.KidsPort, name='KidsPort'),
    path("OceanSandbox/", views.OceanSandbox, name='OceanSandbox'),
    path("PizzaPlace/", views.PizzaPlace, name='PizzaPlace'),
    path("Theater/", views.Theater, name='Theater'),
    path("TugBoats/", views.TugBoats, name='TugBoats'),
    path("Vet/", views.Vet, name='Vet'),
    path("Waters/", views.Waters, name='Waters'),
    path("Temp/", views.Temp, name='Temp'),
    path("FamilyPlayProject/", views.FamilyPlayProject, name='FamilyPlayProject'),
    path("Publix/", views.Publix, name='Publix'),
    path("SafetyVillage/", views.SafetyVillage, name='SafetyVillage'),
    path("Play/", views.Play, name='Play'),
    path("Resources/", views.Resources, name='Resources'),
    path("PartyPlace/", views.PartyPlace, name='PartyPlace'),
    path('admin/', admin.site.urls),
    path('Account/', views.Account, name='Account'),
    path('get_activities/', views.get_activities, name='get_activities'),
]
