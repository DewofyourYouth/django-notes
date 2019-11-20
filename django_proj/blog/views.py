from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date

posts = [
    {
        'author': 'Yaakov Shore',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': date(2018, 7, 5)
    },
    {
        'author': 'Chani Shore',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': date(2019, 7, 5)
    }
]

# Create your views here.


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
