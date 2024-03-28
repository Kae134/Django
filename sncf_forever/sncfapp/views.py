from django.shortcuts import render

def accueil(request) :
    return render(request, "sncfapp/accueil.html",{})

def creation(request) :
    return render(request, "sncfapp/creation.html",{})

def random(request) :
    return render(request, "sncfapp/random.html",{})

def showall(request) :
    return render(request, "sncfapp/showall.html",{})

def show(request) :
    return render(request, "sncfapp/show.html",{})


