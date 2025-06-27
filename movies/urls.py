from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.movies_view, name='movies.index'),
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
]
