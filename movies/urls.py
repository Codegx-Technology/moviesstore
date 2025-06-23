from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.movies_view, name='movies.index'),
    path('<int:id>/', views.movies_show, name='movies.show'),
]
