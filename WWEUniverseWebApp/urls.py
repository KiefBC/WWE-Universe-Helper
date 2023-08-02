from django.shortcuts import redirect
from django.urls import path

from .views import ComingSoon, IndexWrestlers, IndexShows, UpdateInformation

urlpatterns = [
    path('', ComingSoon.as_view(), name='coming_soon'),
    # add_wrestler/ redirects to coming_soon/
    path('add_wrestler/', lambda request: redirect('coming_soon'), name='add_wrestler'),
    # add_title/ redirects to coming_soon/
    path('add_title/', lambda request: redirect('coming_soon'), name='add_title'),
    # add_show/ redirects to coming_soon/
    path('add_show/', lambda request: redirect('coming_soon'), name='add_show'),
    # we use this to run our reset_db command
    path('run_reset/', ComingSoon.run_db_reset, name='run_reset'),
    # this is for listing off all of our wrestlers
    path('wrestlers/', IndexWrestlers.as_view(), name='list_wrestlers'),
    # for listing off all of our shows
    path('shows/', IndexShows.as_view(), name='list_shows'),
    # updating our wrestlers
    # path('update_stats/', lambda request: redirect('list_wrestlers'), name='update_stats'),
    path('update_stats/', UpdateInformation.as_view(), name='update_stats'),
]
