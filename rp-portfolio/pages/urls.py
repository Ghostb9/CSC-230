# pages/urls.py

from django.urls import path
from pages import views
from .views import tos_tracker_view

urlpatterns = [
    path('track-tos/', tos_tracker_view, name='track-tos'),
    path("", views.home, name='home'),
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
    path("LearningCenter/", views.LearningCenter, name='LearningCenter'),
    path("OceanSandbox/", views.OceanSandbox, name='OceanSandbox'),
    path("PizzaPlace/", views.PizzaPlace, name='PizzaPlace'),
    path("Theater/", views.Theater, name='Theater'),
    path("TugBoats/", views.TugBoats, name='TugBoats'),
    path("Vet/", views.Vet, name='Vet'),
    path("Waters/", views.Waters, name='Waters'),
    path("GuestService/", views.GuestServices, name='GuestServices'),
    path("Temp/", views.Temp, name='Temp'),
    path("FamilyPlayProject/", views.FamilyPlayProject, name='FamilyPlayProject'),
    path("Publix/", views.Publix, name='Publix'),
]

