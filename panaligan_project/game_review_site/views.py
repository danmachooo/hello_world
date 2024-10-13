from django.shortcuts import render

def home(request):
    return render(request, 'reviews/home.html')

def reviews(request):
    return render(request, 'reviews/reviews.html')

def about(request):
    return render(request, 'reviews/about.html')
