from django.urls import path
from . import views

app_name = 'home'

urlpatterns =[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('movies-list/', views.movie_list, name='movie-list'),
]