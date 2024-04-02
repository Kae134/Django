from django.shortcuts import render

def accueil(request) :
    return render(request, "sncf_app/accueil.html",{})

def creation(request) :
    return render(request, "sncf_app/creation.html",{})

def random(request) :
    return render(request, "sncf_app/random.html",{})

def showall(request) :
    return render(request, "sncf_app/show-all.html",{})

def show(request):
    return render(request, "sncf_app/show.html", {})