from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)

    def __str__(self):
        return self.title
