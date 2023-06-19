from django.contrib.gis import forms
from .models import Deplacement, Lieu, Societe, Site, Profil, Mode, Motif, Raison, Type
from django.db.models import Q


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class deplacementsForm(forms.ModelForm):
    class Meta:
        model = Deplacement
        exclude = ('utilisateur',)
        widgets = {
            'date': DateInput(),
            'heure_depart': TimeInput(),
            'heure_arrivee': TimeInput(),
        }
        labels = {
            'date':'Date du déplacement',
            'heure_depart':'Heure de départ',
            'heure_arrivee':'Heure d\'arrivée',
            'lieu_depart':'De',
            'lieu_arrivee':'À',
            'mode':'Mode de déplacement principal',
            'motif':'Motif du déplacement',
            'raison':'Raison du choix du mode de déplacement (sélectionner celle qui semble la plus pertinente)',
        }

    def __init__(self, user, *args, **kwargs):
        self.utilisateur = user
        super(deplacementsForm, self).__init__(*args, **kwargs)
        self.fields['lieu_depart'].queryset = Lieu.objects.filter(Q(utilisateur=user) | Q(utilisateur=1)).order_by('-utilisateur', 'nom')
        self.fields['lieu_arrivee'].queryset = Lieu.objects.filter(Q(utilisateur=user) | Q(utilisateur=1)).order_by('-utilisateur', 'nom')
        self.fields['lieu_depart'].empty_label = "Sélectionner"
        self.fields['lieu_arrivee'].empty_label = "Sélectionner"
        self.fields['mode'].empty_label = "Sélectionner"
        self.fields['mode'].queryset = Mode.objects.order_by('nom_mode')
        self.fields['motif'].empty_label = "Sélectionner"
        self.fields['motif'].queryset = Motif.objects.order_by('nom_motif')
        self.fields['raison'].empty_label = "Sélectionner"
        self.fields['raison'].queryset = Raison.objects.order_by('nom_raison')

class ajout_lieuForm(forms.ModelForm):
    class Meta:
        model = Lieu      
        exclude = ('rue', 'no_entree', 'npa', 'localite', 'utilisateur',)
        widgets = {
            'coord': forms.OSMWidget(attrs={'map_width': 500, 'map_height': 300, 'default_lon':8.2, 'default_lat':46.8,'default_zoom':7, }),
        }
        labels = {
            'nom':'Nom du lieu qui apparaîtra dans la liste des déplacements (exemple: "Domicile" ou "Localité, chantier Xxx")',
            'type':'Type du lieu',
            'no_entree':'Numéro de l\'entrée',
            'npa':'NPA',
            'localite':'Localité',
            'coord': ''
        }

    def __init__(self, user, *args, **kwargs):
        self.utilisateur = user
        super(ajout_lieuForm, self).__init__(*args, **kwargs)
        self.fields['type'].empty_label = "Sélectionner"
        self.fields['type'].queryset = Type.objects.order_by('nom_type')

class infos_utilisateurForm(forms.ModelForm):
    class Meta:
        model = Profil
        exclude = ('utilisateur',)
        labels = {
            'societe':'Pour quelle société travaillez-vous principalement ?',
            'site':'Sur quel site travaillez-vous principalement ?',
            'fonction':'À quel type de fonction appartenez-vous ?',
            'taux':'À quel taux travaillez-vous ?',
            'teletravail':'Combien de jours complets de télétravail allez-vous effectuer entre le 24 avril et le 5 mai 2023 ?',
            'pmr':'Êtes-vous une personne à mobilité réduite (personne ayant des besoins particuliers en terme de mobilité) ?',
            'bike_to_work':'Participez-vous à l\'événement Bike to work ?',
        }    
    
    def __init__(self, user, *args, **kwargs):
        self.utilisateur = user        
        super(infos_utilisateurForm, self).__init__(*args, **kwargs)
        self.fields['societe'].empty_label = "Sélectionner"
        self.fields['societe'].queryset = Societe.objects.order_by('nom_societe')
        self.fields['site'].empty_label = "Sélectionner"
        self.fields['site'].queryset = Site.objects.order_by('nom_site')
        self.fields['fonction'].empty_label = "Sélectionner"
        self.fields['taux'].empty_label = "Sélectionner"
        self.fields['teletravail'].empty_label = "Sélectionner"