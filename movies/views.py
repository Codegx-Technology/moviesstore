from tempfile import template
from django.shortcuts import render

movies = [
    {'id': 1, 'name': "Titanic", 'description': "Love story", "price": "$12"},
    {'id': 2, 'name': "Avatar", 'description': "Suspense thriller", "price": "$30"},
]

def movies_view(request):
    template_data = {
        'title': "Movies",
        'movies': movies   
    }
    return render(request, 'movies/movies.html', {'template_data': template_data})