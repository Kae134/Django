from django.shortcuts import render, redirect
from sncfapp.models import Trains
from random import randint
import sys  

def accueil(request) :
    return render(request, "sncfapp/accueil.html",{})

def creation(request) :
    return render(request, "sncfapp/creation.html",{})

def save_train(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        departure = request.POST.get('departure')
        arrive = request.POST.get('arrive')
        destination = request.POST.get('destination')
        description = request.POST.get('description')
        
        # Enregistrer le nouveau train dans la base de données
        Trains.objects.create(
            name=name,
            departure=departure,
            arrive=arrive,
            destination=destination,
            description=description
        )
        
        # Redirection vers une page de confirmation ou une autre vue
        return showall() # Rediriger vers une vue qui affiche la liste des trains
        
    return showall()  # Rediriger vers le formulaire d'ajout en cas de méthode incorrecte ou d'échec

def random(request) :
    All_trains = Trains.objects.all()
    Taille = len(All_trains)
    
    if Taille != 0 :
        rand_num = randint(1, Taille-1)
        i = 0
        for Train in All_trains :
            if i == rand_num :
                return show_train(request, Train.trainId)
            i += 1
    else :
        return show_train(request, None)

def showall(request) :
    return render(request, "sncfapp/showall.html",{
        'trains':Trains.objects.all()
        })

def show(request) :
    return render(request, "sncfapp/show.html",{})

def show_train(request, id):
    try :  
        Train = Trains.objects.get(trainId=id)  
        return render(request, "sncfapp/show.html", {
            'train':Train,
        })
        
    except :
            try :
                Train = Trains.objects.get(name=id) 
                return render(request, "sncfapp/show.html", {
                    'train':Train,
                })
            except :
                return render(request, 'sncfapp/train_not_found.html')
    

def history(request) :
    return render(request, "sncfapp/history.html",{})


def process_train(request) :
    if request.method == 'POST':
        try :
            train_request = request.POST.get('train_request')
            return show_train(request, train_request)
        except :
            return showall(request)
    else:
        return showall(request)
