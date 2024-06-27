from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(
            Q(title__icontains=query) | Q(genre__icontains=query)
        )
    else:
        movies = Movie.objects.all()
        
    paginator = Paginator(movies, 5)

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    
    context = {
        'movies': movies,
    }
    return render(request, 'movies/home.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})