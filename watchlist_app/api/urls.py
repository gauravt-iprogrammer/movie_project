from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import MovielistAV, MoviedetailsAV


urlpatterns = [
    path('list/',MovielistAV.as_view(), name='movie-list'),
    path('<int:pk>',MoviedetailsAV.as_view(), name='movie-details')
]