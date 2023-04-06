from rest_framework import serializers
from deplacements.models import Lieu, Site, Societe, Deplacement, Mode, Motif, Raison
#from deplacements.models import Lieu, Site, Societe, Domicile, Deplacement, Mode, Motif, Raison

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lieu
        fields='__all__'

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Site
        fields='__all__'

class SocieteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Societe
        fields='__all__'

class DeplacementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Deplacement
        fields='__all__'

class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mode
        fields='__all__'

class MotifSerializer(serializers.ModelSerializer):
    class Meta:
        model=Motif
        fields='__all__'

class RaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Raison
        fields='__all__'
