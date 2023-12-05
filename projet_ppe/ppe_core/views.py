from django.shortcuts import render
from django.http import HttpResponse
from .models import Personnage
from django.template import loader



def index(request):
    personnage_list = Personnage.objects.all()
    template = loader.get_template("ppe_core/index.html")
    context = {
        "personnage_list": personnage_list,
    }
    return HttpResponse(template.render(context, request))


def derniers_personnages(request):
    latest_personnage_list = Personnage.objects.order_by("id")[:5]
    template = loader.get_template("ppe_core/personnage_list.html")
    context = {
        "latest_personnage_list": latest_personnage_list,
    }
    return HttpResponse(template.render(context,request))


def afficher_personnage_text(request, personnage_id):
    
    template = loader.get_template("ppe_core/personnage_text.html")
    context = {
        "personnage": Personnage.objects.get(id=personnage_id)
    }
    output = Personnage.objects.get(id=personnage_id)

    return HttpResponse(template.render(context,request))