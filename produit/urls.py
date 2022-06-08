from django.contrib import admin
from produit.views import *
from django.urls import path, include
from django_filters.views import FilterView
from . import views

urlpatterns=[
    path('acceuil/', views.acceuil,name="acceuil"),
    path('render/pdf/',Panier2.as_view(), name="panier2"),
    path('eshop/', views.eshop,name="eshop"),
    path('vitrine/', views.vitrine,name="vitrine"),
  
    path('panier/', views.supprimerall,name="supprimerall"),
    path('equivalant/', views.equivalant,name="equivalant"),
    path('details/<str:pk>', views.details, name='details'),
    path('panier2/',Panier2.as_view(),name="panier2"),
    path('panier/<str:pk>/',views.supprimercommande,name="supprimercommande"),
    path('inscription/', views.inscriptionPage,name="inscriptionPage"),
    path('inscription2/', views.inscriptionPage2,name="inscriptionPage2"),
    path('login/', views.login,name="login"),
    path('login2/', views.login2,name="login2"),
    path('panier/<str:id>/', views.modif,name="modif" ),
    path('quitter/', views.logoutUser,name="quitter"),
    path('chercherarticle/', home1.as_view(), name='home1'),
    path('catalogue/', achat.as_view(), name='achat'),
    path('commande/', commande.as_view(), name='commande'),
    
    

   

    
    ]