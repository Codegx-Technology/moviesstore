from tempfile import template
from django.shortcuts import render

movies = [
    {
        'id': 1, 'name': 'Inception', 'price': 12,
        'description': 'A mind-bending heist thriller.'
    },
    {
        'id': 2, 'name': 'Avatar', 'price': 13,
        'description': 'A journey to a distant world'
    },
    {
        'id': 3, 'name': 'The Dark Knight', 'price': 14,
        'description': 'Gothams vigilante faces the Joker.'
    },
    {
        'id': 4, 'name': 'Titanic', 'price': 11,
        'description': 'A love story set against the',
    },
]

def movies_view(request):
    template_data = {
        'title': "Movies",
        'movies': movies   
    }
    return render(request, 'movies/movies.html', {'template_data': template_data})

def movies_show(request, id):
    movie = next((movie for movie in movies if movie['id'] == id), None)
    if not movie:
        return render(request, '404.html', status=404)
    
    template_data = {
        'title': "Movies",
        'movie': movie
    }
    return render(request, 'movies/show.html', {'template_data': template_data})