from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    movie_type = models.CharField(max_length=200, default='action')
    image = models.ImageField(upload_to="images/", default="images/none/noimage.jpg")

    def __str__(self):
        return self.name
