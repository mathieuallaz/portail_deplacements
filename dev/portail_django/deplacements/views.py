from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http.response import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from deplacements.models import Lieu, Site, Societe, Domicile, Deplacement, Mode, Motif, Raison
from deplacements.serializers import LieuSerializer, SiteSerializer, SocieteSerializer, DomicileSerializer, DeplacementSerializer, ModeSerializer, MotifSerializer, RaisonSerializer

# Create your views here.

#@csrf_exempt
#def index(request):
    #return render(request, 'InfosApp/index.html')

class LieuViewSet(viewsets.ModelViewSet):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = (IsAuthenticated, )

class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = (IsAuthenticated, )

class SocieteViewSet(viewsets.ModelViewSet):
    queryset = Societe.objects.all()
    serializer_class = SocieteSerializer

class DomicileViewSet(viewsets.ModelViewSet):
    queryset = Domicile.objects.all()
    serializer_class = DomicileSerializer
    permission_classes = (IsAuthenticated, )

class DeplacementViewSet(viewsets.ModelViewSet):
    queryset = Deplacement.objects.all()
    serializer_class = DeplacementSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields =['date', 'utilisateur']
    search_fields = ['utilisateur']

class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer
    permission_classes = (IsAuthenticated, )

class MotifViewSet(viewsets.ModelViewSet):
    queryset = Motif.objects.all()
    serializer_class = MotifSerializer
    permission_classes = (IsAuthenticated, )

class RaisonViewSet(viewsets.ModelViewSet):
    queryset = Raison.objects.all()
    serializer_class = RaisonSerializer
    permission_classes = (IsAuthenticated, )

@csrf_exempt
def societeApi(request,id=0):
    if request.method =='GET':
        societe = Societe.objects.all()
        societe_serializer=SocieteSerializer(societe,many=True)
        return JsonResponse(societe_serializer.data,safe=False)
    elif request.method=='POST':
        societe_data=JSONParser().parse(request)
        societe_serializer=SocieteSerializer(data=societe_data)
        if societe_serializer.is_valid():
            societe_serializer.save()
            return JsonResponse("Correctement ajoutée", safe=False)
        return JsonResponse("Echec de l'ajout", safe=False)
    elif request.method=='PUT':
        societe_data=JSONParser().parse(request)
        societe = Societe.objects.get(Id_societe=societe_data['Id_societe'])
        societe_serializer=SocieteSerializer(societe,data=societe_data)
        if societe_serializer.is_valid():
            societe_serializer.save()
            return JsonResponse("Mise à jour avec succès",safe=False)
        return JsonResponse("Echec de la mise à jour")
    elif request.method=='DELETE':
        societe=Societe.objects.get(Id_societe=id)
        societe.delete()
        return JsonResponse("Correctement supprimée",safe=False)
