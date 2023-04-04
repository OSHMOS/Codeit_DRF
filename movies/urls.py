from django.urls import path
from .views import movie_list, movie_detail, actor_list

urlpatterns = [
    path('movies', movie_list, name='movies'),
    path('movies/<int:pk>', movie_detail),
    path('actors', actor_list),
]
