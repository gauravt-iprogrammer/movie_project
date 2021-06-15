from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework import status

# Views for streaming 
class StreamPlatformAV(APIView):
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serialize = StreamPlatformSerializer(platform, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = StreamPlatformSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailsAV(APIView):
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Data not available"}, status=status.HTTP_404_NOT_FOUND)
            
        serialize = StreamPlatformSerializer(platform)
        return Response(serialize.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serialize = StreamPlatformSerializer(platform, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serialize = StreamPlatformSerializer(platform, data=request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class based views
class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serialize = WatchListSerializer(movies, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = WatchListSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailsAV(APIView):

    def get(self, request, pk):
        try:
            movies = WatchList.objects.get(pk=pk)
        
        except WatchList.DoesNotExist:
            return Response({"Error": "Data not available"}, status=status.HTTP_404_NOT_FOUND)
        
        serialize = WatchListSerializer(movies)
        return Response(serialize.data)

    def put(self, request, pk):
        
        movies = WatchList.objects.get(pk=pk)
        serialize = WatchListSerializer(movies, data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):

        movies = WatchList.objects.get(pk=pk)
        serialize = WatchListSerializer(movies, data=request.data, partial=True)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        movies = WatchList.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        


# Work done using function based views
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serialize = MovieSerializer(movies, many=True)
#         return Response(serialize.data)
    
#     if request.method == 'POST':
#         serialize = MovieSerializer(data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET','PUT','DELETE','PATCH'])
# def movie_details(request, pk):
    
#     if request.method == 'GET':
#         try:
#             movies = Movie.objects.get(pk=pk)
        
#         except Movie.DoesNotExist:
#             return Response({"Error": "Data not available"}, status=status.HTTP_404_NOT_FOUND)
        
#         serialize = MovieSerializer(movies)
#         return Response(serialize.data)
    
#     if request.method == 'PUT':
       
#         movies = Movie.objects.get(pk=pk)
#         serialize = MovieSerializer(movies, data=request.data)

#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status=status.HTTP_202_ACCEPTED)
        
#         else:
#             return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)



#     if request.method == 'DELETE':
#         movies = Movie.objects.get(pk=pk)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     if request.method == 'PATCH':
#         movies = Movie.objects.get(pk=pk)
#         serialize = MovieSerializer(movies, data=request.data, partial=True)

#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status=status.HTTP_206_PARTIAL_CONTENT)
#         else:
#             return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

