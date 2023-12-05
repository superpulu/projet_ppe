from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("personnage", views.derniers_personnages, name="derniers_personnages"),
    path("personnage/<int:personnage_id>/", views.afficher_personnage_text, name="personnage_detail_text")
]