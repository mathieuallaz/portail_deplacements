from django.contrib.auth.models import User
from rest_framework import serializers
from deplacements.models import Lieu, Site, Societe, Profil, Fonction, Taux, Deplacement, Mode, Motif, Raison, Teletravail, Type

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

class PofilSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profil
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = PofilSerializer(source='profil')
    class Meta:
        fields='__all__'

class FonctionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fonction
        fields='__all__'

class TauxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Taux
        fields='__all__'

class TeletravailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teletravail
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

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type
        fields='__all__'
