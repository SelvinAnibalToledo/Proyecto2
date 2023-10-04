from django.db import models

class Studio(models.Model):
    name = models.CharField(max_length=30)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    country = models.CharField(max_length=60)
    description= models.TextField()
    GenreType= models.TextChoices("GenreType", "Adventure Drama Sci-Fi Comedy Action Fantasy Horror")
    genre = models.CharField(blank=False, choices=GenreType.choices, max_length=18)
    studio = models.ForeignKey(Studio,on_delete=models.SET_NULL, null=True)

class Prueba(models.Model):
    name = models.CharField(max_length=30)