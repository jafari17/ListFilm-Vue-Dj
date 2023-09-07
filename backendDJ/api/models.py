from django.db import models


class Projects(models.Model):
    film = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField(default=1999)
    star = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.film