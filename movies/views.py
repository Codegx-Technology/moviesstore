from tempfile import template
from django.shortcuts import render

movies = [
    {'id': 1, 'name': "Titanic", 'description': "Love story", "price": "$12"},
    {'id': 2, 'name': "Avatar", 'description': "Suspense thriller", "price": "$30"},
    {'id': 3, 'name': "Inception", 'description': "Mind-bending thriller", "price": "$15"},
    {'id': 4, 'name': "The Godfather", 'description': "Crime drama", "price": "$20"},
    {'id': 5, 'name': "The Dark Knight", 'description': "Superhero action", "price": "$18"},
    {'id': 6, 'name': "Pulp Fiction", 'description': "Cult classic", "price": "$10"},
    {'id': 7, 'name': "Forrest Gump", 'description': "Inspirational drama", "price": "$14"},
    {'id': 8, 'name': "The Shawshank Redemption", 'description': "Prison drama", "price": "$16"},
    {'id': 9, 'name': "Schindler's List", 'description': "Historical drama", "price": "$22"},
    {'id': 10, 'name': "The Matrix", 'description': "Sci-fi action", "price": "$25"}
]

def movies_view(request):
    template_data = {
        'title': "Movies",
        'movies': movies   
    }
    return render(request, 'movies/movies.html', {'template_data': template_data})