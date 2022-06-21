# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime
from pickle import FLOAT
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from MySQLdb.constants.FLAG import UNSIGNED
from datetime import date
User = get_user_model()

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    # insert other fields here
class Temp(models.Model):
    id= models.AutoField(primary_key=True)
    COD_ART=models.CharField(max_length=50)
    user_name=models.CharField(max_length=50)
    quantité=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True,null=True)
    prix_vente_ht = models.CharField(max_length=20)
    taux_tva = models.CharField(max_length=10)
    prix_vente_ttc = models.FloatField()
    totalqte = models.IntegerField()
    prix_vente_promotion = models.CharField(max_length=20)
  
    def total(self):
        if self.prix_vente_ttc is not None :
            return round(self.quantité * (self.prix_vente_ttc), 2)
    class Meta:
        managed = False
        db_table = 'temp'
class Article2(models.Model):
    id_article = models.AutoField(primary_key=True)
    code_famille = models.CharField(db_column='Code_famille', max_length=20)  # Field name made lowercase.
    cod_art = models.CharField(db_column='COD_ART', max_length=20)  # Field name made lowercase.
    des_art = models.TextField(db_column='DES_ART')  # Field name made lowercase.
    oem= models.CharField(db_column='OEM', max_length=20) 
    cod_bar_fab = models.CharField(db_column='COD_BAR_FAB', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cod_bar_int = models.CharField(db_column='COD_BAR_INT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taux_tva = models.CharField(max_length=10)
    marge = models.CharField(max_length=10)
    casier = models.CharField(max_length=10, blank=True, null=True)
    unite = models.CharField(max_length=10, blank=True, null=True)
    qte_stock = models.CharField(max_length=20)
    qte_min = models.CharField(max_length=10, blank=True, null=True)
    qte_max = models.CharField(max_length=10, blank=True, null=True)
    reliquat = models.CharField(db_column='Reliquat', max_length=10, blank=True, null=True)  # Field name made lowercase.
    qte_initiale = models.CharField(max_length=20)
    qte_promotion = models.CharField(max_length=20, blank=True, null=True)
    qte_emballage_vente = models.CharField(max_length=20, blank=True, null=True)
    qte_emballage_achat = models.CharField(max_length=20)
    prix_achat_ht = models.CharField(max_length=20)
    prix_vente_ht = models.CharField(max_length=20)
    aprix_achat_ht = models.CharField(db_column='Aprix_achat_ht', max_length=20)  # Field name made lowercase.
    prix_vente_promotion = models.CharField(max_length=20)
    a_prix_vente_ht = models.CharField(db_column='A_prix_vente_ht', max_length=20)  # Field name made lowercase.
    prix_vente_ttc = models.FloatField()
    prix_achat_ttc = models.CharField(max_length=20)
    prix_achat_devise = models.CharField(max_length=20)
    adaptable = models.CharField(max_length=10, blank=True, null=True)
    equivalence = models.CharField(max_length=20, blank=True, null=True)
    photo = models.CharField(max_length=10, blank=True, null=True)
    deroi_consommation = models.CharField(max_length=20, blank=True, null=True)
    article_compose = models.CharField(max_length=20, blank=True, null=True)
    code_fournisseur = models.CharField(max_length=20, blank=True, null=True)
    sans_code_abarre = models.CharField(max_length=20, blank=True, null=True)
    avec_fodec = models.CharField(max_length=10, blank=True, null=True)
    mode = models.CharField(max_length=10, blank=True, null=True)
    complement_de_prix = models.CharField(max_length=20)
    date_creation = models.CharField(max_length=20, blank=True, null=True)
    qte_promotion_achat = models.CharField(max_length=20, blank=True, null=True)
    prix_achat_promotion = models.CharField(max_length=20)
    taux_vente = models.CharField(max_length=10, blank=True, null=True)
    prix_achat_sansremise = models.CharField(max_length=30)
    qte_initiale_anneepre = models.CharField(max_length=30, blank=True, null=True)
    remise = models.CharField(max_length=10)
    qte_encours = models.CharField(max_length=20, blank=True, null=True)
    sans_stock = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=20, blank=True, null=True)
    dernier_vente = models.CharField(max_length=20, blank=True, null=True)
    dernier_achat = models.CharField(max_length=20, blank=True, null=True)
    prix_achat_moyen = models.CharField(max_length=20)
    aprix_achat_moyen = models.CharField(db_column='Aprix_achat_moyen', max_length=20)  # Field name made lowercase.
    color_article = models.CharField(max_length=10, blank=True, null=True)
    poids = models.CharField(max_length=10)
    unite_cart = models.CharField(max_length=10, blank=True, null=True)
    categorie = models.CharField(max_length=10, blank=True, null=True)
    marques = models.CharField(max_length=10, blank=True, null=True)
    code_douane = models.CharField(max_length=20, blank=True, null=True)
    remise_achat = models.CharField(max_length=20)
    remise_vente = models.CharField(max_length=20)
    prix_public = models.CharField(max_length=20)
    ref_frs = models.CharField(max_length=10, blank=True, null=True)
    remise_max = models.CharField(max_length=10)
    prix_vente_min = models.CharField(max_length=20)
    avec_fodec_achat = models.CharField(max_length=20, blank=True, null=True)
    preferentiel = models.CharField(max_length=20, blank=True, null=True)
    date_periem = models.CharField(max_length=20, blank=True, null=True)
    pub_web = models.CharField(max_length=10, blank=True, null=True)
    code_gfamille = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article2'



class FamilleArticle(models.Model):
    code_famille = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=50)
    id = models.IntegerField()
    marge = models.IntegerField()
    avec_fodec = models.CharField(max_length=50)
    taux_tva = models.FloatField(db_column='taux_TVA')  # Field name made lowercase.
    ordre = models.IntegerField()
    code_fournisseur = models.CharField(max_length=50)
    aff_equi = models.CharField(max_length=50)
    cod_art = models.CharField(max_length=50)
    mp = models.CharField(db_column='MP', max_length=50)  # Field name made lowercase.
    pf = models.CharField(db_column='PF', max_length=50)  # Field name made lowercase.
    code_gfamille = models.CharField(max_length=50)
    pub_web = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'famille_article'
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)

class Cart(models.Model): 
    customer=models.OneToOneField(Customer, null=True, on_delete=models.CASCADE) 
    article_panier=models.ManyToManyField(Article2)    
 
    def __str__(self):
        return str(self.customer)

class Commande(models.Model):
    id_commande= models.AutoField(primary_key=True)
    COD_ART=models.CharField(max_length=50)
    user_name=models.CharField(max_length=50)
    quantité=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True,null=True)
    total = models.FloatField()
    prix_vente_ttc = models.FloatField()
    class Meta:
        managed = False
        db_table = 'commande'
class GrandFamille(models.Model):
    id_gfamille = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    pub_web = models.CharField(max_length=50)
    date_modification = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grand_famille'
