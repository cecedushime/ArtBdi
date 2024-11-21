from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView
from .forms import UserRegistrationForm 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models.signals import post_save
from .models import Profil
from .forms import UserProfilForm
from django.contrib.auth.decorators import login_required
from .models import Oeuvre_art
from .forms import Oeuvre_artForm



def home(request):
    return render(request, 'artapp/home.html')

def login_user(request):
    if request.method == 'POST':
       username = request.POST["username"]
       password = request.POST["password"]
       user = authenticate(request, username = username, password = password)
       
       if user is not None:
           login(request, user)
           return redirect("appart:home")
       else:
           messages.info(request, "Identifiant ou mot de passe incorrect")
                  
    form = AuthenticationForm()
    return render(request, "artapp/login.html",{"form": form})
    
def logout_user(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect("appart:home")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            

            # Connexion automatique de l'utilisateur
            login(request, user)
            
            messages.success(request, "Inscription réussie ! Bienvenue.")
            
            return redirect('appart:home')
    else:
        form = UserRegistrationForm()
    return render(request, "artapp/register.html", {'form': form})

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profil, user=user)
    
    if request.method == 'POST':
        form = UserProfilForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=request.user.username)  # Redirige avec le nom d'utilisateur
    else:
        form = UserProfilForm(instance=profile)

    return render(request, 'artapp/profil.html', {'form': form, 'user': user})



def profile_edit_view(request, user_id):
    user_profile = Profil.objects.get(user__id=user_id)

    if request.method == 'POST':
        form = UserProfilForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=user_profile.user.username)
    else:
        form = UserProfilForm(instance=user_profile)
    
    return render(request, 'profile_edit.html', {'form': form})





  


def all_artworks(request):
    artworks = Oeuvre_art.objects.all()
    return render(request, "all_artworks.html", {'artworks':artworks})

def artwork_detail(request, id):
    artwork = get_object_or_404(Oeuvre_art, id=id)
    return render(request, "artwork_detail.html", {'artwork': artwork})

class HomeView(ListView):
    model = Oeuvre_art
    template_name = 'home.html'
    context_object_name = 'artworks'
    ordering = ['-date_posted']  # Order artworks by date posted
    paginate_by = 10  # Show 10 artworks per page

def create_oeuvre(request):
    if request.method == 'POST':
        form = Oeuvre_artForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('oeuvre_list')
        
        else:
            form = Oeuvre_artForm()
        return render(request, 'create_oeuvre.html',{'form': form})

def edit_oeuvre(request, oeuvre_id):
    oeuvre = get_object_or_404(Oeuvre_art, id=oeuvre_id)
    if request.method == 'POST':
        form = Oeuvre_artForm(request.POST, request.FILES, instance=oeuvre)
        if form.is_valid():
            form.save()
            return redirect('oeuvre_list')
        else:
            form = Oeuvre_artForm(instance=oeuvre)
        return render(request, 'edit_oeuvre.html', {'form': form})       

def delete_oeuvre(request, oeuvre_id):
    oeuvre = get_object_or_404(Oeuvre_art, id=oeuvre_id)
    if request.method == 'POST':
        oeuvre.delete()
        return redirect('oeuvre_list')
    return render(request, 'delete_oeuvre.html', {'oeuvre': oeuvre})

def place_order(request, id):
    artwork = get_object_or_404(Oeuvre_art, id=id)
    
    
    return render(request, 'order_comfirmation.html', {'artwork': artwork})

def request_rental(request, id):
    artwork = get_object_or_404(Oeuvre_art, id=id)
    
    if request.method == 'POST':
        # Ici, vous pouvez traiter la demande de loction
        # Par exemple, enregistrer les detals de location dans la base de donnees
        # Pour cet exemple, nous allons rediriger vers une page de confirmation
        return render(request, 'rental_confirmation.html', {'artwork': artwork})
    return render(request, 'rental_request.html', {'artwork': artwork})