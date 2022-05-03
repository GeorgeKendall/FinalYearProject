from django.shortcuts import render
from django.http import HttpResponse
import csv
import sys
csv.field_size_limit(sys.maxsize)
from .models import *

def initial_page(request):
    movs = MovieProfile.objects.all()
    if movs.count() != 914: 
        print("Loading movies...")
        # Need to save objs from csv to DB
        with open('data/ddump_soup.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Create a MovieProfile instance
                obj = MovieProfile(
                    poster_path = row['Poster_Link'],
                    title = row['Series_Title'],
                    genre = row['Genre'],
                    overview = row['Overview'],
                    director = row['Director'],
                    s1 = row['Star1'],
                    s2 = row['Star2'],
                    s3 = row['Star3'],
                    s4 = row['Star4'],
                    soup = row['Soup'],
                )
                obj.save()   
    # otherwise assume all items are saved  
    test = {}
    for i, item in enumerate(movs):
        test[i+1] = item.to_dict() # to index from 1 (like db)
    # print(test[1]['title'])
    return render(request, 'home.html', {'movs': test,})

