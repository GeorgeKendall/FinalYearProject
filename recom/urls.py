from django.urls import path

from . import views
from .api import *


urlpatterns = [
    path('', views.initial_page, name=''),

    path('api/movs/', get_all, name='get_all'),
    path('api/movie/', get_mov, name='get_mov'),
    path('api/movie/check?', check_exist, name="check_exist"),
    path('api/movie/recom?', get_recom, name="get_recom"),
]