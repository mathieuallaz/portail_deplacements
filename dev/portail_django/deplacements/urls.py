from django.urls import path, re_path
from deplacements import views

from django.conf import settings # to import static in deployment
from django.conf.urls.static import static # to import static in deployment


urlpatterns = [
    path('', views.authentification, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('accueil', views.accueil, name='accueil'),
    path('consignes', views.consignes, name='consignes'),
    path('deplacements/', views.deplacements, name="deplacements"),
    path('deplacements/ajout_deplacement/', views.ajout_deplacement, name='ajout_deplacement'),
    path('deplacements/edition_deplacement/<int:id>/', views.ajout_deplacement, name='edition_deplacement'),
    path('deplacements/recup_deplacement/<int:id>/', views.recup_deplacement, name='recup_deplacement'),
    path('deplacements/supprimer_deplacement/<int:id>/', views.supprimer_deplacement, name='supprimer_deplacement'),
    path('lieux/', views.lieux, name='lieux'),
    path('lieux/ajout_lieu/', views.ajout_lieu, name='ajout_lieu'),
    path('lieux/edition_lieu/<int:id>/', views.ajout_lieu, name='edition_lieu'),
    path('infos/', views.infos_utilisateur, name='infos_utilisateur'),
    path('infos/ajout_infos/', views.edition_infos, name='ajout_infos'),
    path('infos/edition_infos/<int:id>/', views.edition_infos, name='edition_infos'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # to import static in deployment
