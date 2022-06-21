from email.message import EmailMessage
from re import M
import turtle
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from logging import Filterer
from msilib.schema import SelfReg
#from typing_extensions import Self
from django.shortcuts import render
from multiprocessing import context
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from graphviz import view
from produit.forms import produitForm
from produit.filtre import ArticleFiltre
from produit.models import Article2,Temp,Commande
from django.views import View
from flask import redirect, request
from django.db.models import Q
from django.db.models import F
from django.contrib import messages 
from produit.forms import UpdateproduitForm,panierForm
from django.db.models.signals import pre_save
from turtle import update
from django.dispatch import receiver
from .InscriptionForms import InscriptionForms
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.db.models import Sum
from  django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
#import mysql.connector
from pyexpat.errors import messages
from operator import itemgetter
from django.shortcuts import (get_object_or_404,
                            render,
                            HttpResponseRedirect)
from datetime import datetime
import numpy as np
from django.core.mail import EmailMultiAlternatives
#@login_required(login_url='login/')
from django.core.mail import EmailMessage
from .process import Render
from django.template.loader import render_to_string
import csv
from io import StringIO
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from .process import *
import requests
from threading import Thread, activeCount
from django.views.generic import View

from .models import *
from .process import *
from threading import Thread, activeCount
def send_email(file: list):
    r = requests.post(
  
    files=[("attachment", (file[0], open(file[1], "rb").read()))],
    data={"from": "rahmamaalej1234@gmail.com",
    "to": "rahmamaalej1234@gmail.com",
    "subject": "Sales Report",
    "text": "Requested Sales Report",
    "html": "<html>Requested Sales Report</html>"})
class Panier2(View):
    def get(self, request):
        print('get')
        my_orders = Temp.objects.using('user').filter(user_name=request.session['username'])
        article=Article2.objects.using('user').all()
        for x2 in my_orders:
            
            art=Article2.objects.using('user').get(cod_art = x2.COD_ART) 
            print(art.prix_vente_ttc)
            return render(request,'panier2.html',{'aa':my_orders,'art':art})
        
        return render(request,'panier2.html',{'aa':my_orders})

    def post(self, request):
        
        form=produitForm(request.POST)
        print("post") 
        
        my_orders = Temp.objects.using('user').filter(user_name=request.session['username'])
        #aa=Temp.objects.using('user').filter(id=id).update(;;; =request.POST.get('quantité'))
        
        print(request.POST )
        
        ca = (request.POST.getlist('COD_ART'))
        qn = (request.POST.getlist('quantité'))
        
        print("post")
        c=  request.session['username']
        rahma=Temp.objects.using('user').all()    
        for item in range(len(ca)):
            print(ca[item])
            
            ww= Temp.objects.using('user').filter(COD_ART=ca[item],user_name=c).first()
           
            Temp.objects.using('user').filter(pk=ww.id).update(quantité = qn[item])

            
            #zz = Temp.objects.using('user').get(pk=t.id)
    
        for x in my_orders:

            print(x)
            b=  x.quantité 
            a=	x.COD_ART
            p=	x.prix_vente_ttc
            m=	request.POST.get('total')
            c=  request.session['username'] 
            com = Commande.objects.using('user').create(quantité=b,COD_ART=a,user_name=c,prix_vente_ttc=p,total=m)
            com.save()
         
            assigned_leads = Temp.objects.using('user').filter(user_name=request.session['username']).distinct()
            csvfile = StringIO()
            csvwriter = csv.writer(csvfile)
            for leads in assigned_leads:
                csvwriter.writerow(['Code article', 'quantité'])
                csvwriter.writerow([leads.COD_ART, leads.quantité])
            message = EmailMessage("Commande","Votre commande","myemail@gmail.com",["rahmamaalej1234@gmail.com"])
            message.attach('commande.csv', csvfile.getvalue(), 'text/csv')
            message.send()
            #sales = Temp.objects.using('user').filter(user_name=request.session['username']).distinct()
            
            '''params = {
      
            'sales': sales,
            'request': request
            }'''
            '''msg = EmailMultiAlternatives('mail_subject', 'text_content', settings.DEFAULT_FROM_EMAIL, ["rahmamaalej1234@gmail.com"])
            msg.attach_alternative(message, "text/html")
            pdf = render_to_pdf('pdf.html',params)
            msg.attach('invoice.pdf', pdf)
            msg.send()'''
           
            
            '''email = EmailMessage('Subject here', 'Here is the message.', 'from@me.com', ["rahmamaalej1234@gmail.com"])
            email.attach_alternative(message, "text/html")
            pdf = render_to_pdf('pdf.html',params)
            email.attach_file('invoice.pdf',pdf)
            email.send()'''
            
            #return Render.render('pdf.html', params)
            '''file = Render.render_to_file('pdf.html', params)
            thread = Thread(target=send_email, args=(file,))
            thread.start()
            return HttpResponse("Processed")'''
            record = Temp.objects.using('user').get(id = x.id)
            record.delete()
            #x.objects.using('user').delete()
            return  render(request,'panier2.html',{'form':form})
     
        

     
class commande(View):
    def get(self, request):
        print('get')
        sales = Commande.objects.using('user').filter(user_name=request.session['username']).distinct()
        my_orders = Commande.objects.using('user').filter(user_name=request.session['username'])
        my_orders2 = Temp.objects.using('user').filter(user_name=request.session['username'])  
        params = {
      
            'sales': sales,
            'request': request
            } 
        f= Render.render('pdf.html', params)
        return render(request,'commande.html',{'cc':my_orders,'aa':my_orders2,'f':f})

def modif( request,id):
   
    monpanier = Temp.objects.using('user').filter(user_name=request.session['username'])
    aa=Temp.objects.using('user').filter(id=id).update(quantité =request.POST.get('quantité'))
   
    print(request)
    print(request.GET)
    print(request.POST)
    form = panierForm()
    
    return render(request,'panier2.html',{'cc':monpanier,'form':form,'aa':aa})
           





# update view for details
'''def modifier(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Temp, id = id)

    # pass the object as instance in form
    form = panierForm(request.POST or None, instance = obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form
    
    return render(request, "panier.html", context)'''

def  supprimercommande(request,pk):
    
    panier= Temp.objects.using('user').get(id=pk)
    
    print('here')
    panier.delete()
    
    
    return  HttpResponseRedirect('/panier2/')
def  supprimerall(request):
    
    panier= Temp.objects.using('user').all()
    
    print('here')
    panier.delete()
    
    
    return  HttpResponseRedirect('/panier2/')




def index(request):
    return render(request,'index1.html')

def presentation(request):
    return render(request,'presentation.html')
    
def logoutUser(request):
    logout(request)
    return redirect('vitrine')

def login2(request):
    form = InscriptionForms()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None :
            auth_login(request,user)
            request.session['username']= username
            print(request.session['username'])
            return  HttpResponseRedirect('/eshop/')
        else:
            messages.info(request,"Utilisateur et/ou mot de passe n'est pas valide")
            return render(request,'login2.html',{'form':form})
    return render(request,'login2.html',{'form':form})
def login(request):
    form = InscriptionForms()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None :
            auth_login(request,user)
            request.session['username']= username
            print(request.session['username'])
            return  HttpResponseRedirect('/eshop/')
        else:
            messages.info(request,"Utilisateur et/ou mot de passe n'est pas valide")
            return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})

@login_required(login_url='login')
def acceuil (request):
    my_orders = Temp.objects.using('user').filter(user_name=request.session['username'])
    form = panierForm()
    #request.session['user'] = 'omar'
    #print(request.session['user'])
    return render(request,'acceuil.html',{'aa':my_orders,'form':form})
def eshop (request):
    my_orders = Temp.objects.using('user').filter(user_name=request.session['username'])
    #request.session['user'] = 'omar'
    #print(request.session['user'])
    form = panierForm()

    return render(request,'eshop.html',{'aa':my_orders,'form':form})       
def cart(request):
    #request.session['user'] = 'omar'
    #print(request.session['user'])
    return render(request,'panier2.html') 
def catalogue (request):
    #request.session['user'] = 'omar'
    #print(request.session['user'])
    return render(request,'catalogue.html')   
   
def equivalant (request):
    
    
    return render(request,'equivalant.html')   
def vitrine(request):
    
    
    return render(request,'vitrine.html')   
   
def details(request, pk):
    try:
        book = Article2.objects.using('user').get(pk=pk)
    except  Article2.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'details.html', context={'book': book})
'''
 def get_total(self):
        if self.product.discount_percent > 0:
            price_now = self.product.price - self.product.price * self.product.discount_percent / 100
        else:
            price_now = self.product.price
 
        total = price_now * self.quantity
        return total
        TTC = HT x (1 + ([taux de TVA] / 100))
'''
    
class achat(View):
    context={}
    form = produitForm()
    template_name = 'catalogue.html'
    
    def get(self,request  ,*args, **kwargs):
        rahma=Article2.objects.using('user').all()
        template_name = 'catalogue.html'
        self.context['rahma']='rahma'
        form=produitForm(request.POST)
        self.context['form']=form
        try :
            print(request.GET['search'])
            print (122222)
            print(request.GET['selected'])
            print (20000)
        except :
            print (1)
        #f= Article2.object.get('code famille','DES_ART')
        f = ArticleFiltre(request.GET, queryset=Article2.objects.using('user').all())    
        my_orders = Temp.objects.using('user').filter(user_name=request.session['username'])   
        try:     
            if (len(request.GET['code_famille'])==0):
                q1= (Article2.objects.using('user').filter(Q(des_art__contains=request.GET['des_art'])))&(Article2.objects.filter(Q(cod_art__contains=request.GET['cod_art'])))&(Article2.objects.filter(Q(oem__contains=request.GET['oem'])))&(Article2.objects.filter(Q(equivalence__contains=request.GET['equivalence'])))
               
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1,'aa':my_orders})
            elif (len(request.GET['des_art'])==0):
                q1= (Article2.objects.using('user').filter(Q(code_famille__contains=request.GET['code_famille'])))&(Article2.objects.filter(Q(cod_art__contains=request.GET['cod_art'])))&(Article2.objects.filter(Q(oem__contains=request.GET['oem'])))&(Article2.objects.filter(Q(equivalence__contains=request.GET['equivalence'])))
                 
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1,'aa':my_orders})
            elif (len(request.GET['cod_art'])==0):
                q1= (Article2.objects.using('user').filter(Q(code_famille__contains=request.GET['code_famille'])))&(Article2.objects.filter(Q(des_art__contains=request.GET['des_art'])))&(Article2.objects.filter(Q(oem__contains=request.GET['oem'])))&(Article2.objects.filter(Q(equivalence__contains=request.GET['equivalence'])))
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1,'aa':my_orders})
            elif (len(request.GET['oem'])==0):
                q1= (Article2.objects.using('user').filter(Q(code_famille__contains=request.GET['code_famille'])))&(Article2.objects.filter(Q(des_art__contains=request.GET['des_art'])))&(Article2.objects.filter(Q(equivalence__contains=request.GET['equivalence'])))
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1,'aa':my_orders})
            elif (len(request.GET['oem'])==0):
                q1= (Article2.objects.using('user').filter(Q(code_famille__contains=request.GET['code_famille'])))&(Article2.objects.filter(Q(des_art__contains=request.GET['des_art'])))
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1,'aa':my_orders})
            elif (len(request.GET['code_famille'])!=0) and (len(request.GET['des_art'])!=0 ) and (len(request.GET['cod_art'])!=0):
                q1=(Article2.objects.using('user').filter (Q(code_famille__contains=request.GET['code_famille'])))& (Article2.objects.filter(Q(des_art__contains=request.GET['des_art'])))& (Article2.objects.filter(Q(cod_art__contains=request.GET['cod_art'])))&(Article2.objects.filter(Q(oem__contains=request.GET['oem'])))&(Article2.objects.filter(Q(equivalence__contains=request.GET['equivalence'])))
                 
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1,'aa':my_orders})
            else:
                return("data is empty")

    
            
        except:
            print("omar")
            return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'aa':my_orders})
    def post(self,request,*args, **kwargs):
        my_orders = Temp.objects.using('user').filter(user_name=request.session['username'])   
        print('yes')
        print(request.POST)
        rahma=Temp.objects.using('user').all()   
        
        template_name = 'catalogue.html'
       
        form=produitForm()
        
        a=  request.POST.get('cod_art')
        v=  request.POST.get('prix_vente_ht')
        
        b=  request.POST.get('quantité') 
        m=  request.POST.get('prix_vente_promotion') 
        #m=request.GET.get('prix_vente_ttc')
        
        #n=request.GET.get('taux_tva') 
        #m=request.REQUEST.GET.get(Article2, 'prix_vente_ttc  ')
        #queryset = (Article2.objects.using('user').filter(Q(cod_art=request.GET.get('prix_vente_ttc'))))
        #print(queryset)
        #queryset2 = (Article2.objects.using('user').filter(Q(cod_art=request.GET.get('taux_tva'))))
        d= Temp(date=datetime.now() )
        
        c=  request.session['username']
        print(a,c,b)
        try :
            rahmaa= Temp.objects.using('user').filter(COD_ART=a,user_name=c).first()
             
            Temp.objects.using('user').filter(pk=rahmaa.id).update(quantité =F('quantité') +b)
            
            
            print(rahmaa.quantité)
             
             
            print('om')
            
        except :
           art=Article2.objects.using('user').get(cod_art = a) 
           print(art.prix_vente_ttc)
        

           rahmaa= Temp.objects.using('user').create(COD_ART=a,quantité=b,user_name=c,date=d,prix_vente_ht=v,prix_vente_ttc=art.prix_vente_ttc,prix_vente_promotion=m)
           rahmaa.save()
            
        f = ArticleFiltre(request.GET, queryset=Article2.objects.using('user').all())       
        try:
            
                
                
            if (len(request.GET['code_famille'])==0):
                q1= (Article2.objects.using('user').filter(Q(des_art__contains=request.GET['des_art'])))&(Article2.objects.filter(Q(cod_art__contains=request.GET['cod_art'])))&(Article2.objects.filter(Q(oem__contains=request.GET['oem'])))
            elif (len(request.GET['oem'])==0):
                q1= (Article2.objects.using('user').filter(Q(des_art__contains=request.GET['des_art'])))&(Article2.objects.filter(Q(cod_art__contains=request.GET['cod_art'])))
               
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1,'aa':my_orders})
            elif (len(request.GET['des_art'])==0):
                q1= (Article2.objects.using('user').filter(Q(code_famille__contains=request.GET['code_famille'])))&(Article2.objects.filter(Q(cod_art__contains=request.GET['cod_art'])))&(Article2.objects.filter(Q(oem__contains=request.GET['oem'])))
               
                 
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1,'aa':my_orders})
            elif (len(request.GET['cod_art'])==0):
                q1= (Article2.objects.using('user').filter(Q(code_famille__contains=request.GET['code_famille'])))&(Article2.objects.filter(Q(des_art__contains=request.GET['des_art'])))&(Article2.objects.filter(Q(oem__contains=request.GET['oem'])))
               
                 
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1,'aa':my_orders})
            elif (len(request.GET['code_famille'])!=0) and (len(request.GET['des_art'])!=0 ) and (len(request.GET['cod_art'])!=0):
                q1=(Article2.objects.using('user').filter (Q(code_famille__contains=request.GET['code_famille'])))& (Article2.objects.filter(Q(des_art__contains=request.GET['des_art'])))& (Article2.objects.filter(Q(cod_art__contains=request.GET['cod_art'])))&(Article2.objects.filter(Q(oem__contains=request.GET['oem'])))
               
                 
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1,'aa':my_orders})
            else:
                return("data is empty")

    
            
        except:
            print("omar")
            return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'aa':my_orders})
      
       

       
def inscriptionPage(request):
    form=InscriptionForms()
    print(request.POST)
    if request.method=='POST':
        form=InscriptionForms(request.POST)
        if form.is_valid():
            form.save()
            #user=form.cleaned_data.get('username')
            #messages.success(request,'compte crrée avec succes'+user)        
    context={'form':form}
    return render(request,'inscription.html',context)

def inscriptionPage2(request):
    form=InscriptionForms()
    print(request.POST)
    if request.method=='POST':
        form=InscriptionForms(request.POST)
        if form.is_valid():
            form.save()
            #user=form.cleaned_data.get('username')
            #messages.success(request,'compte crrée avec succes'+user)    
            return  HttpResponseRedirect('/login2/')    
    context={'form':form}
    return render(request,'inscription2.html',context)


class home1(View):
    context={}
    form = produitForm()
    template_name = 'ajouterarticle.html'
    def get(self, request, *args, **kwargs):
        rahma=Article2.objects.using('user').all()
        template_name = 'chercherarticle.html'
        
        self.context['rahma']='rahma'
        form=produitForm(request.POST)
        self.context['form']=form
        #f= Article2.object.get('code famille','DES_ART')
        f = ArticleFiltre(request.GET, queryset=Article2.objects.using('user').all())
        try:
                
                
            if (len(request.GET['code_famille'])==0):
                q1= (Article2.objects.using('user').filter(Q(des_art__contains=request.GET['des_art'])))&(Article2.objects.filter(Q(cod_art__contains=request.GET['cod_art'])))
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1})
            elif (len(request.GET['des_art'])==0):
                q1= (Article2.objects.using('user').filter(Q(code_famille__contains=request.GET['code_famille'])))&(Article2.objects.filter(Q(cod_art__contains=request.GET['cod_art'])))
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1})
            elif (len(request.GET['cod_art'])==0):
                q1= (Article2.objects.using('user').filter(Q(code_famille__contains=request.GET['code_famille'])))&(Article2.objects.filter(Q(des_art__contains=request.GET['des_art'])))
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1})
            elif (len(request.GET['code_famille'])!=0) and (len(request.GET['des_art'])!=0 ) and (len(request.GET['cod_art'])!=0):
                q1=(Article2.objects.using('user').filter (Q(code_famille__contains=request.GET['code_famille'])))& (Article2.objects.filter(Q(des_art__contains=request.GET['des_art'])))& (Article2.objects.filter(Q(cod_art__contains=request.GET['cod_art'])))
                return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f,'q1': q1})
            else:
                return("data is empty")


            
        except:
            
            print("omar")
            
            return render (request,template_name ,{'form': form,'rahma': rahma, 'filter': f})

