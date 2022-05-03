from http.client import HTTPResponse
from telnetlib import STATUS
from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404

from .recom import *

from .models import *

def get_all(request):
    '''
        get entire dictionary of movies:
        to display all on original page load??
    '''
    return JsonResponse({
        'movs': [
            mov.to_dict()
            for mov in MovieProfile.objects.all()
        ]
    })

def get_mov(request):
    '''
        get single movie dict items:
        to show on 'focusmovie' section
    '''
    if request.is_ajax and request.method == "GET":
        title = request.GET['title']
        movie = MovieProfile.objects.get(title = title)
    return JsonResponse(movie.to_dict())

def check_exist(request):
    '''
        return status code for single movie item
    '''
    if request.is_ajax and request.method == 'GET':
        if MovieProfile.objects.filter(title = request.GET['title']).exists():
            return HTTPResponse(STATUS=302)
        else:
            return HTTPResponse(STATUS=404)

def get_recom(request):
    '''
        get 5 movie dict items:
        recoms of focus movie
    '''
    title = request.GET['title']
    result = recommend(title)
    # Now to get list of MovieProfile Objs
    final = {}
    keys = range(4)
    for i in keys:
        final[i] = MovieProfile.objects.get(title = result[i]).to_dict()
    return JsonResponse({
        'recom': final,
    })