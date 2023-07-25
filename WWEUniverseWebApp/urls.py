from django.urls import path
from .views import ComingSoon
from django.shortcuts import redirect

urlpatterns = [
    path('', ComingSoon.as_view(), name='coming_soon'),
    # add_wrestler/ redirects to coming_soon/
    path('add_wrestler/', lambda request: redirect('coming_soon'), name='add_wrestler'),
    # add_title/ redirects to coming_soon/
    path('add_title/', lambda request: redirect('coming_soon'), name='add_title'),
    # add_show/ redirects to coming_soon/
    path('add_show/', lambda request: redirect('coming_soon'), name='add_show'),
    path('run_reset/', ComingSoon.run_db_reset, name='run_reset'),
    ]