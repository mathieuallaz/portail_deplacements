from django.contrib.gis import forms
from .models import Deplacement, Lieu, Profil


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class deplacementsForm(forms.ModelForm):
    class Meta:
        model = Deplacement
        fields = '__all__' #('', '', '')
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
            'mode':'Mode de déplacement',
            'motif':'Motif du déplacement',
            'raison':'Raison du choix du mode de déplacement',
        }

    def __init__(self, *args, **kwargs):
        super(deplacementsForm, self).__init__(*args, **kwargs)
        self.fields['lieu_depart'].empty_label = "Sélectionner"
        self.fields['lieu_arrivee'].empty_label = "Sélectionner"
        self.fields['mode'].empty_label = "Sélectionner"
        self.fields['motif'].empty_label = "Sélectionner"
        self.fields['raison'].empty_label = "Sélectionner"
        self.fields['utilisateur'].empty_label = "Sélectionner"
        #self.fields[''].required = False

class ajout_lieuForm(forms.ModelForm):
    class Meta:
        model = Lieu
        fields = ('nom', 'rue', 'no_entree', 'npa', 'localite', 'coord',)        
        widgets = {
            'coord': forms.OSMWidget(attrs={'map_width': 500, 'map_height': 300,}),
        }
        labels = {
            'nom':'Nom du lieu',
            'no_entree':'Numéro de l\'entrée',
            'npa':'NPA',
            'localite':'Localité',
            'coord': ''
        }

class infos_utilisateurForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = '__all__' #('', '', '')
        labels = {
            'societe':'Pour quelle société travaillez-vous principalement ?',
            'site':'Sur quel site travaillez-vous principalement ?',
            'fonction':'À quel type de fonction appartenez-vous ?',
            'taux':'À quel taux travaillez-vous ?',
            'pmr':'Êtes-vous une personne à mobilité réduite (personne ayant des besoins particuliers en terme de mobilité) ?',
            'bike_to_work':'Participez-vous à l\'événement Bike to work ?',
        }    
    
    def __init__(self, *args, **kwargs):
        super(infos_utilisateurForm, self).__init__(*args, **kwargs)
        self.fields['societe'].empty_label = "Sélectionner"
        self.fields['site'].empty_label = "Sélectionner"
        self.fields['fonction'].empty_label = "Sélectionner"
        self.fields['taux'].empty_label = "Sélectionner"
        self.fields['utilisateur'].empty_label = "Sélectionner"