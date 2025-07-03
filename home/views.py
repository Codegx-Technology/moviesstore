# home/views.py
from django.shortcuts import render
from . models import Movie

def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    return render(request, 'home/index.html', {'template_data': template_data})

def about(request):
    return render(request, 'home/about.html')

def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')

def contact_us(request):
    return render(request, 'home/contact_us.html' )

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'home/movie_list.html', {'movie_list':movies})