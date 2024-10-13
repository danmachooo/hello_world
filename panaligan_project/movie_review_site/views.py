# movie_review/views.py
from django.shortcuts import render

def movie_list(request):
    return render(request, 'movie_review/movie_list.html')

def review_create(request):
    return render(request, 'movie_review/review_form.html')

def review_detail(request, review_id):
    # For demonstration, we'll just return static content based on review_id
    return render(request, 'movie_review/review_detail.html', {'review_id': review_id})
