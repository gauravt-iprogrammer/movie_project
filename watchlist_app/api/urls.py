from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchDetailsAV,
StreamPlatformDetailsAV, StreamPlatformAV, ReviewList, ReviewDetails, ReviewCreate)


urlpatterns = [
    path('list/',WatchListAV.as_view(), name='movie-list'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('<int:pk>',WatchDetailsAV.as_view(), name='movie-details'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-details'),
    # path('review/', ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>', ReviewDetails.as_view(), name='review-details')
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='reviewstream-details'),
    path('stream/review/<int:pk>', ReviewDetails.as_view(), name='review-details')

]