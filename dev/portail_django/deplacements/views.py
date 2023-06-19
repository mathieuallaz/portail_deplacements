from django.shortcuts import render, redirect
from .forms import deplacementsForm, ajout_lieuForm, infos_utilisateurForm
from .models import Deplacement, Lieu, Profil

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def authentification(request):
    context = {}
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.info(request, "Nom d'utilisateur et/ou mot de passe incorrects")
    return render(request, "deplacements/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def accueil(request):
    return render(request, "deplacements/accueil.html")

@login_required(login_url='login')
def consignes(request):
    return render(request, "deplacements/consignes.html")

@login_required(login_url='login')
def deplacements(request):
    context = {'deplacements':Deplacement.objects.filter(utilisateur=request.user).order_by('date','heure_depart')}
    return render(request, "deplacements/deplacements.html", context)

@login_required(login_url='login')
def ajout_deplacement(request, id=0):
    if request.method =='GET':
        if id==0:
            form = deplacementsForm(request.user)
        else:
            deplacement = Deplacement.objects.get(pk=id)
            form = deplacementsForm(request.user, instance=deplacement)
        return render(request, "deplacements/ajout_deplacement.html", {'form':form})
    else:
        if id==0:
            form = deplacementsForm(request.user, request.POST)
        else:
            deplacement = Deplacement.objects.get(pk=id)
            form = deplacementsForm(request.user, request.POST, instance=deplacement)
        if form.is_valid():
            deplacement = form.save(commit=False)
            deplacement.utilisateur = request.user
            deplacement.save()
        return redirect('/deplacements')
    
@login_required(login_url='login')
def recup_deplacement(request, id=0):
    deplacement = Deplacement.objects.get(pk=id)
    deplacement.id_deplacement = None
    deplacement.save(force_insert=True)
    return redirect('/deplacements')
    
@login_required(login_url='login')
def supprimer_deplacement(request,id):
    deplacement = Deplacement.objects.get(pk=id)
    deplacement.delete()
    return redirect('/deplacements')

@login_required(login_url='login')
def lieux(request):
    context = {'lieux':Lieu.objects.filter(utilisateur=request.user).order_by('nom')}
    return render(request, "deplacements/lieux.html", context)

@login_required(login_url='login')
def ajout_lieu(request, id=0):
    if request.method =='GET':
        if id==0:
            form = ajout_lieuForm(request.user)
        else:
            lieu = Lieu.objects.get(pk=id)
            form = ajout_lieuForm(request.user, instance=lieu)
        return render(request, "deplacements/ajout_lieu.html", {'form':form})
    else:
        if id==0:
            form = ajout_lieuForm(request.user, request.POST)
        else:
            lieu = Lieu.objects.get(pk=id)
            form = ajout_lieuForm(request.user, request.POST, instance=lieu)
        if form.is_valid():
            lieu = form.save(commit=False)
            lieu.utilisateur = request.user
            lieu.save()
        return redirect('/lieux')

@login_required(login_url='login')
def infos_utilisateur(request):
    context = {'infos_utilisateur':Profil.objects.filter(utilisateur=request.user)}
    return render(request, "deplacements/infos_utilisateur.html", context)

@login_required(login_url='login')
def edition_infos(request, id=0):
    if request.method =='GET':
        if id==0:
            form = infos_utilisateurForm(request.user)
        else:
            profil = Profil.objects.get(pk=id)
            form = infos_utilisateurForm(request.user, instance=profil)
        return render(request, "deplacements/edition_infos.html", {'form':form})
    else:
        if id==0:
            form = infos_utilisateurForm(request.user, request.POST)
        else:
            profil = Profil.objects.get(pk=id)
            form = infos_utilisateurForm(request.user, request.POST, instance=profil)
        if form.is_valid():
            infos_utilisateur = form.save(commit=False)
            infos_utilisateur.utilisateur = request.user
            infos_utilisateur.save()
        return redirect('/infos')

    
