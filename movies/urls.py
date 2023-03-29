from django.urls import path
from .views import movie_list, actor_list

urlpatterns = [
    path('movies', movie_list, name='movies'),
    path('actors', actor_list),
]
