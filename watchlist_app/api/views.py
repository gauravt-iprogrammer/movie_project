from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serialize = MovieSerializer(movies, many=True)
        return Response(serialize.data)
    
    if request.method == 'POST':
        serialize = MovieSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)



@api_view(['GET','PUT','DELETE','PATCH'])
def movie_details(request, pk):
    
    if request.method == 'GET':
        movies = Movie.objects.get(pk=pk)
        serialize = MovieSerializer(movies)
        return Response(serialize.data)
    
    if request.method == 'PUT':
        movies = Movie.objects.get(pk=pk)
        serialize = MovieSerializer(movies, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)



    if request.method == 'DELETE':
        movies = Movie.objects.get(pk=pk)
        movies.delete()
        return Response("Data deleted")
    
    if request.method == 'PATCH':
        movies = Movie.objects.get(pk=pk)
        serialize = MovieSerializer(movies, data=request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)

