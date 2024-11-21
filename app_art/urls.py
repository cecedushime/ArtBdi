from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static





app_name = "appart"

urlpatterns = [
    path('', views.home, name= 'home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('profile_view/<str:username>/', views.profile_view, name='profile_view'),
    path('profile_edit_view/', views.profile_edit_view, name='profile_edit'),
    path('logout/', views.logout_user , name= 'logout'),
    path('all_artworks/',views.all_artworks, name='all_artworks'),
    path('artwork_detail/<int:id>/',views.artwork_detail, name='artwork_detail'),
    path('artwork/<int:id>/order/', views.place_order, name='place_order'),
    path('artwork/<int:id>/rental/', views.request_rental, name='request_rental'),
    path('oeuvre/create/',views.create_oeuvre, name='create_oeuvre'),
    path('oeuvre/edit/<int:oeuvre_id>/',views.edit_oeuvre, name='edit_oeuvre'),
    path('oeuvre/delete/<int:oeuvre_id>/',views.delete_oeuvre, name='delete_oeuvre'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
