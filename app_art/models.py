from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist






class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=30, null=True)
    
    def __str__(self) :
        return f"{self.adresse}"
    
    
class Artistes(models.Model):
    id = models.AutoField(primary_key=True)
    pseudounymes = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    contact = models.CharField(max_length= 254)
    photo = models.ImageField(upload_to='images/')
    visible = models.BooleanField(default=False)
    def __str__(self) :
        return f"{self.contact} {self.pseudounymes}"
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    date_de_naissance = models.DateField(null=True, blank=True)
    image_de_profil = models.ImageField(upload_to='images/', default='images/default.jpg')
    
    
    def get_user_info(self):
        try:
            return self.user.profil
        except ObjectDoesNotExist:
            return None

    def __str__(self):
        return self.user.username
     
     
      

    
class Oeuvre_art(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    is_for_sale = models.BooleanField(default=True)
    is_for_rent = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    pseudo = models.OneToOneField(User, editable=True ,null=True,on_delete=models.CASCADE)
    def __str__(self) :
        return f"{self.image} {self.description}"
    
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    oeuvre_art = models.ForeignKey("Oeuvre_art", on_delete=models.CASCADE,default=1)
    quantite_initiale = models.FloatField(default=0)
    quantite_actuelle = models.FloatField(editable=False, null=True)
    
    def __str__(self) :
        return f"{self.quantite_initiale} {self.quantite_actuelle}"
    

    
class Categorie(models.Model):
        id = models.AutoField(primary_key=True)
        nom = models.CharField(max_length=255)
        oeuvre_art = models.ForeignKey("Oeuvre_art",on_delete=models.CASCADE,default=0)
        description = models.TextField(blank=True)
        
        def __str__(self) :
            return f"{self.nom}"  
    
    

    


class Panier(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    oeuvre_art = models.ForeignKey("Oeuvre_art", on_delete=models.CASCADE,default=0)
    quantite = models.PositiveIntegerField(default=1)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return f"{self.quantite}"    

    
class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    oeuvre_art = models.ForeignKey("Oeuvre_art", on_delete=models.CASCADE,default=0)
    client = models.ForeignKey("Clients", on_delete=models.CASCADE,default=0)
    class Statut(models.CharField):
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
      
    def __str__(self) :
        return f"{self.date}"  

class En_Location(models.Model):
    id = models.AutoField(primary_key=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)
   
    def __str__(self) :
        return f"{self.date_debut} {self.date_fin}"
    

      
    
    
    

    
    
    
    
    
    