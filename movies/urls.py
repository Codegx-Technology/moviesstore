from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.movies_view, name='index'),
    path('<int:id>/', views.movies_show, name='show'),
]
