# home/views.py
from django.shortcuts import render

def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    return render(request, 'home/index.html', {'template_data': template_data})

def about(request):
    template_data = {'title': 'About Us'}
    return render(request, 'home/about.html', template_data)