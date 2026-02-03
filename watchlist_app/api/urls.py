from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformListAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-details'),
    path('platforms/', StreamPlatformListAV.as_view(), name='Platform-list'),
    path('platforms/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
]