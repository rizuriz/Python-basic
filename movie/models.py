from django.db import models

class Movie(models.Model):
    actor = models.CharField(max_length=20)
    actor_movie = models.CharField(max_length=30)
    genre = models.CharField(max_length=20)
    movie_logo = models.CharField(max_length=100)

    def __str__(self):
        return self.actor + '=' + self.actor_movie

class song(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    song_name = models.CharField(max_length=100)

    def __str__(self):
        return self.song_name