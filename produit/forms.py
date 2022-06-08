from hello_world.forms import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
class produitForm(forms.Form):
    id_article = forms.IntegerField()
    des_art = forms.IntegerField()
    code_famille=forms.CharField
    COD_ART = forms.CharField()  # Field name made lowercase.
    cod_bar_fab = forms.CharField()  # Field name made lowercase.
    cod_bar_int = forms.CharField()  # Field name made lowercase.
    taux_tva = forms.FloatField()  # Field name made lowercase.
    unité = forms.CharField()
    qte_stock = forms.IntegerField()
    quantité = forms.IntegerField()
    qte_promotion = forms.IntegerField()
    prix_vente_promotion = forms.FloatField()
    prix_vente_ht = forms.FloatField()
    qte_emballage_vente = forms.IntegerField()
    prix_vente_ttc = forms.FloatField()
    photo = forms.CharField()
    avec_fodec = forms.CharField()
    qte_encours = forms.IntegerField()
    description = forms.CharField()
    poids = forms.IntegerField()
    unite_cart = forms.IntegerField()
    categorie = forms.CharField()
    marque = forms.CharField()
    preferentiel = forms.CharField()
    pub_web = forms.CharField()
    code_gfamille = forms.CharField()
    remise_vente = forms.FloatField()
    date_modification = forms.DateField()
    reliquat = forms.IntegerField()
    user_name=forms.CharField()
    quantité=forms.IntegerField()
class panierForm (forms.Form):
    COD_ART=forms.CharField()
    user_name=forms.CharField()
    quantité=forms.IntegerField()
    
    class Meta:
         fields = [ 'COD_ART','quantité','user_name']
class UpdateproduitForm(forms.ModelForm):
    des_art  = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    COD_ART = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        
        fields = ['des_art', 'COD_ART']