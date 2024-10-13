# movie_review/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('review/new/', views.review_create, name='review_create'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
]
