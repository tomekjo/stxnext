from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField(max_length=2030)
    duration = models.CharField(max_length=10)
    rate = models.IntegerField
    director = models.CharField(max_length=128)
    Genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
