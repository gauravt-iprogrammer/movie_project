from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailsAV,StreamPlatformDetailsAV, StreamPlatformAV


urlpatterns = [
    path('list/',WatchListAV.as_view(), name='movie-list'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('<int:pk>',WatchDetailsAV.as_view(), name='movie-details'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-details')
]