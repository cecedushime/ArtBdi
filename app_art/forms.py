from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil
from .models import Oeuvre_art

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class UserProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('bio','date_de_naissance','image_de_profil',)

class Oeuvre_artForm(forms.ModelForm):
    class Meta:
        model = Oeuvre_art
        fields = ('titre','description','prix','image','pseudo',)