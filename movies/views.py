from tempfile import template
from django.shortcuts import render, get_object_or_404
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
    movie = get_object_or_404(Movie, id=id)
    template_data = {
        'title': movie.title,
        'movie': movie
    }
    return render(request, 'movies/show.html', {'template_data': template_data})