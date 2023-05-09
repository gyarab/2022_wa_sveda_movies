from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    avg_rating = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True)
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)
    genres = models.ManyToManyField('Genre', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.year})"

    def genres_display(self):
        return ", ".join([i.name for i in self.genres.all()])


class Director(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.birth_year})"


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField(blank=True, null=True)
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.birth_year})"


class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
