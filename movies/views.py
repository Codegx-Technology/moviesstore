from tempfile import template
from django.shortcuts import render
from home.models import Movie  # Import the Movie model

# Removed dummy movies list


def movies_view(request):
    movies = Movie.objects.all()  # Fetch all movies from the database
    template_data = {
        'title': "Movies",
        'movies': movies
    }
    return render(request, 'movies/movies.html', {'template_data': template_data})

def movie_detail(request, id):
    movie = None  # Placeholder, will fetch from DB in next step
    if not movie:
        return render(request, 'movies/movie_not_found.html', {'id': id})
    
    template_data = {
        'title': '',  # Placeholder
        'movie': movie
    }
    return render(request, 'movies/movie_detail.html', {'template_data': template_data})