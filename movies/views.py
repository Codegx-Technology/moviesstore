from tempfile import template
from django.shortcuts import render
from .models import Movie

movies = [
    {
        'id': 1,
        'name': "Titanic",
        'description': "Love story",
        'price': "$12",
        'director': "James Cameron",
        'duration': "3h 15m",
        'release_year': 1997,
        'rating': "PG-13",
        'image': 'titanic.jpg'
    },
    {
        'id': 2,
        'name': "Avatar",
        'description': "Suspense thriller",
        'price': "$30",
        'director': "James Cameron",
        'duration': "2h 42m",
        'release_year': 2009,
        'rating': "PG-13",
        'image': 'avatar.jpg'
    },
    {
        'id': 3,
        'name': "Inception",
        'description': "Mind-bending thriller",
        'price': "$15",
        'director': "Christopher Nolan",
        'duration': "2h 28m",
        'release_year': 2010,
        'rating': "PG-13",
        'image': 'inception.jpg'
    },
    {
        'id': 4,
        'name': "The Godfather",
        'description': "Crime drama",
        'price': "$20",
        'director': "Francis Ford Coppola",
        'duration': "2h 55m",
        'release_year': 1972,
        'rating': "R",
        'image': 'godfather.jpg'
    },
    {
        'id': 5,
        'name': "The Dark Knight",
        'description': "Superhero action",
        'price': "$18",
        'director': "Christopher Nolan",
        'duration': "2h 32m",
        'release_year': 2008,
        'rating': "PG-13",
        'image': 'dark_knight.jpg'
    },
    {
        'id': 6,
        'name': "Forrest Gump",
        'description': "Inspirational drama",
        'price': "$14",
        'director': "Robert Zemeckis",
        'duration': "2h 22m",
        'release_year': 1994,
        'rating': "PG-13",
        'image': 'forrest_gump.jpg'
    },
    {
        'id': 7,
        'name': "The Shawshank Redemption",
        'description': "Prison drama",
        'price': "$16",
        'director': "Frank Darabont",
        'duration': "2h 22m",
        'release_year': 1994,
        'rating': "R",
        'image': 'shawshank.jpg'
    },
    {
        'id': 8,
        'name': "Schindler's List",
        'description': "Historical drama",
        'price': "$22",
        'director': "Steven Spielberg",
        'duration': "3h 15m",
        'release_year': 1993,
        'rating': "R",
        'image': 'schindlers_list.jpg'
    },
    {
        'id': 9,
        'name': "The Matrix",
        'description': "Sci-fi action",
        'price': "$25",
        'director': "Lana & Lilly Wachowski",
        'duration': "2h 16m",
        'release_year': 1999,
        'rating': "R",
        'image': 'matrix.jpg'
    }
]


def movies_view(request):
    template_data = {
        'title': "Movies",
        'movies': movies   
    }
    return render(request, 'movies/movies.html', {'template_data': template_data})

def movie_detail(request, id):
    movie = next((movie for movie in movies if movie['id'] == id), None)
    if not movie:
        return render(request, 'movies/movie_not_found.html', {'id': id})
    
    template_data = {
        'title': movie['name'],
        'movie': movie
    }
    return render(request, 'movies/movie_detail.html', {'template_data': template_data})