from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
# from rest_framework import mixins

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("You have already  revied for this Show")


        serializer.save(watchlist=movie, review_user=review_user)

# ------------using mixins------------
# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# Model viewsets
class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


# viewsets
# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serialize = StreamPlatformSerializer(data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


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
        movie = WatchList.objects.all()
        serialize = WatchListSerializer(movie, many=True)
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
            movie = WatchList.objects.get(pk=pk)
        
        except WatchList.DoesNotExist:
            return Response({"Error": "Data not available"}, status=status.HTTP_404_NOT_FOUND)
        
        serialize = WatchListSerializer(movie)
        return Response(serialize.data)

    def put(self, request, pk):
        
        movie= WatchList.objects.get(pk=pk)
        serialize = WatchListSerializer(movie, data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):

        movie = WatchList.objects.get(pk=pk)
        serialize = WatchListSerializer(movie, data=request.data, partial=True)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
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

