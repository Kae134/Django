from django.shortcuts import render
from sncfapp.models import Trains
from random import randint


def accueil(request) :
    return render(request, "sncfapp/accueil.html",{})

def creation(request) :
    return render(request, "sncfapp/creation.html",{})

def random(request) :
    Taille = len(Trains.objects.all())
    
    if Taille != 0 :
        return show_id(request, randint(1, Taille))
    else :
        return show_id(request, None)

def showall(request) :
    return render(request, "sncfapp/showall.html",{
        'trains':Trains.objects.all()
        })

def show(request) :
    return render(request, "sncfapp/show.html",{})

def show_id(request, id):
    Train = Trains.objects.get(trainId=id)
    # All_Trains = Trains.objects.all()

    return render(request, "sncfapp/show.html", {
        'train':Train,
    })

