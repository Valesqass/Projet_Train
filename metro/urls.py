from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
#On créer le chemin pour la page principale
    path('train-info-<int:id>/', views.info),
#Le chemin pour les infos de chaque trains 
]


