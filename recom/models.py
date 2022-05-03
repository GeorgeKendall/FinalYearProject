#from msilib.schema import Directory
from django.db import models

'''
    Poster_Link, Series_Title, Released_Year, Certificate, Runtime,	
    Genre, IMDB_Rating, Overview, Meta_score, Director, Star1,	
    Star2, Star3, Star4, No_of_Votes, Gross, Soup
'''

class MovieProfile(models.Model):
    poster_path = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    overview = models.TextField()
    director = models.CharField(max_length=255)
    s1 = models.CharField(max_length=255)
    s2 = models.CharField(max_length=255)
    s3 = models.CharField(max_length=255)
    s4 = models.CharField(max_length=255)
    soup = models.TextField()

    def to_dict(self):
        return {
            'poster_path': self.poster_path,
            'title': self.title,
            'genre': self.genre,
            'overview': self.overview,
            'director': self.director,
            's1': self.s1,
            's2': self.s2,
            's3': self.s3,
            's4': self.s4,
            'soup': self.soup,
        }