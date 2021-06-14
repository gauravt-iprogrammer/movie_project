from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serialize = MovieSerializer(movies, many=True)
    return Response(serialize.data)

@api_view()
def movie_details(request, pk):
    movies = Movie.objects.get(pk=pk)
    serialize = MovieSerializer(movies)
    return Response(serialize.data)