from typing import Any
from django.contrib import admin
from .models import*



admin.site.site_header='ArtBdi'

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display ='user', 'adresse'
    
@admin.register(Artistes)
class ArtistesAdmin(admin.ModelAdmin):
    list_display ='pseudounymes', 'contact', 'photo'
@admin.register(Oeuvre_art)
class Oeuvre_artAdmin(admin.ModelAdmin):    
    list_display ='titre', 'description', 'image', 'prix', 'pseudo'
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display ='oeuvre_art','quantite_initiale','quantite_initiale'
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):  
    list_display ='nom','oeuvre_art','description'      
    
@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display ='client','oeuvre_art','quantite','date_ajout'
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display ='date','oeuvre_art','client'   
        