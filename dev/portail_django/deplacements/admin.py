from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Lieu, Site, Societe, Profil, Fonction, Taux, Deplacement, Mode, Motif, Raison
#from .models import Lieu, Site, Societe, Domicile, Deplacement, Mode, Motif, Raison
# Register your models here.


@admin.register(Lieu)
class LieuAdmin(OSMGeoAdmin):
    list_display = ('nom', 'rue', 'no_entree', 'npa', 'localite', 'coord')
    list_filter = ('localite', )

@admin.register(Site)
class SiteAdmin(OSMGeoAdmin):
    list_display = ('nom_site', 'lieu')
    list_filter = ('lieu', )

@admin.register(Societe)
class SocieteAdmin(OSMGeoAdmin):
    list_display = ('nom_societe',)

class ProfilInLine(admin.StackedInline):
    model = Profil

class ProfilAdmin(UserAdmin):
    inlines = (ProfilInLine, )

admin.site.unregister(User)
admin.site.register(User, ProfilAdmin)

@admin.register(Fonction)
class FonctionAdmin(OSMGeoAdmin):
    list_display = ('nom_fonction','alias_fonction')

@admin.register(Taux)
class TauxAdmin(OSMGeoAdmin):
    list_display = ('taux',)

@admin.register(Deplacement)
class DeplacementAdmin(OSMGeoAdmin):
    list_display = ('date','heure_depart', 'heure_arrivee', 'lieu_depart', 'lieu_arrivee', 'utilisateur', 'mode', 'motif', 'raison')
    list_filter = ('date','lieu_depart', 'lieu_arrivee', 'utilisateur', 'mode', 'motif', 'raison' )

@admin.register(Mode)
class ModeAdmin(OSMGeoAdmin):
    list_display = ('nom_mode','alias_mode')

@admin.register(Motif)
class MotifAdmin(OSMGeoAdmin):
    list_display = ('nom_motif','alias_motif')

@admin.register(Raison)
class RaisonAdmin(OSMGeoAdmin):
    list_display = ('nom_raison','alias_raison')