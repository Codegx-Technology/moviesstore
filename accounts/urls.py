from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register_done/', views.register_done, name='register_done'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]

