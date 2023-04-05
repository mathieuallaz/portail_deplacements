from django.urls import re_path
from deplacements import views
from rest_framework import routers
from deplacements.views import LieuViewSet, DeplacementViewSet


router = routers.DefaultRouter()
router.register('deplacements', DeplacementViewSet)
router.register('lieux', LieuViewSet)

urlpatterns = [
    #re_path('', views.index),
    #re_path(r'^societe$',views.societeApi),
    #re_path(r'^societe/([0-9]+)$',views.societeApi),

    #re_path(r'^collaborateur$',views.collaborateurApi),
    #re_path(r'^collaborateur/([0-9]+)$',views.collaborateurApi),
]
