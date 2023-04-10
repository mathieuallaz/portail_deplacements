from django.shortcuts import render, redirect
from .forms import deplacementsForm, ajout_lieuForm, infos_utilisateurForm
from .models import Deplacement, Lieu, Profil
from django.http.response import JsonResponse
from django.http.response import HttpResponse

# Create your views here.

def accueil(request):
    return render(request, "deplacements/accueil.html")

def deplacements(request):
    context = {'deplacements':Deplacement.objects.all()}
    return render(request, "deplacements/deplacements.html", context)

def ajout_deplacement(request, id=0):
    if request.method =='GET':
        if id==0:
            form = deplacementsForm()
        else:
            deplacement = Deplacement.objects.get(pk=id)
            form = deplacementsForm(instance=deplacement)
        return render(request, "deplacements/ajout_deplacement.html", {'form':form})
    else:
        if id==0:
            form = deplacementsForm(request.POST)
        else:
            deplacement = Deplacement.objects.get(pk=id)
            form = deplacementsForm(request.POST, instance=deplacement)
        if form.is_valid():
            form.save()
        return redirect('/deplacements') #à controler le renvoi
    
def supprimer_deplacement(request,id):
    deplacement = Deplacement.objects.get(pk=id)
    deplacement.delete()
    return redirect('/deplacements') #à controler le renvoi

def ajout_lieu(request, id=0):

    if request.method =='GET':
        if id==0:
            form = ajout_lieuForm()
        else:
            lieu = Lieu.objects.get(pk=id)
            form = ajout_lieuForm(instance=lieu)
        return render(request, "deplacements/ajout_lieu.html", {'form':form})
    else:
        if id==0:
            form = ajout_lieuForm(request.POST)
        else:
            lieu = Lieu.objects.get(pk=id)
            form = ajout_lieuForm(request.POST, instance=lieu)
        if form.is_valid():
            form.save()
        return redirect('/deplacements') #à controler le renvoi

def infos_utilisateur(request, id=0):
    if request.method =='GET':
        if id==0:
            form = infos_utilisateurForm()
        else:
            profil = Profil.objects.get(pk=id)
            form = infos_utilisateurForm(instance=profil)
        return render(request, "deplacements/infos_utilisateur.html", {'form':form})
    else:
        if id==0:
            form = infos_utilisateurForm(request.POST)
        else:
            profil = Profil.objects.get(pk=id)
            form = infos_utilisateurForm(request.POST, instance=profil)
        if form.is_valid():
            form.save()
        return redirect('/deplacements') #à controler le renvoi

    
