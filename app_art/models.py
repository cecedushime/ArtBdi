from django.db import models
from django.contrib.auth.models import User




class Artistes(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pseudounymes = models.CharField(max_length=100)
    contact = models.CharField(max_length= 254)
    photo = models.ImageField(upload_to='images/')
    visible = models.BooleanField(default=False)

class Oeuvre_art(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    prix = models.FloatField()
    artistes = models.ForeignKey(Artistes, on_delete=models.CASCADE)
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    oeuvre_art = models.ForeignKey("Oeuvre_art", on_delete=models.CASCADE)
    quantite_initiale = models.FloatField(default=0)
    quantite_actuelle = models.FloatField(editable=False, null=True)
    

    
class Categorie(models.Model):
        id = models.AutoField(primary_key=True)
        nom = models.CharField(max_length=255)
        description = models.TextField(blank=True)  
    

    
class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nom = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    mot_de_passe = models.CharField(max_length=50)

class Panier(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    date_ajout = models.DateTimeField(auto_now_add=True)    

    
class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    oeuvre_art = models.ForeignKey("Oeuvre_art", on_delete=models.CASCADE)
    client = models.ForeignKey("Clients", on_delete=models.CASCADE)
    class Statut(models.TextChoices):
      CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
     ]

      status = models.CharField(
        max_length=10,
        choices=CHOICES,
        default='PENDING',
      )

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)
   
    
    

      
    
    
    

    
    
    
    
    
    