from django.urls import path, re_path
from deplacements import views
# pour Django REST framework # from rest_framework import routers
# pour Django REST framework # from deplacements.views import LieuViewSet, DeplacementViewSet


# pour Django REST framework # router = routers.DefaultRouter()
# pour Django REST framework # router.register('deplacements', DeplacementViewSet)
# pour Django REST framework # router.register('lieux', LieuViewSet)

urlpatterns = [
    #re_path(r'^societe$',views.societeApi),
    #re_path(r'^societe/([0-9]+)$',views.societeApi),

    path('', views.authentification, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('accueil', views.accueil, name="accueil"),
    path('deplacements/', views.deplacements, name="deplacements"),
    path('deplacements/ajout_deplacement/', views.ajout_deplacement, name="ajout_deplacement"),
    path('deplacements/ajout_deplacement/<int:id>/', views.ajout_deplacement, name='edition_deplacement'),
    path('deplacements/<int:id>/', views.supprimer_deplacement, name='supprimer_deplacement'),
    path('deplacements/ajout_lieu/', views.ajout_lieu, name='ajout_lieu'),
    path('deplacements/infos_utilisateur/', views.infos_utilisateur, name="infos_utilisateur"),
    path('deplacements/ajout_utilisateur/', views.edition_infos, name='ajout_infos'),
    path('deplacements/infos_utilisateur/<int:id>/', views.edition_infos, name='edition_infos'),
]
