from django.db import models
from django.contrib.auth.models import User


RATING_CHOICES = [
    ('G', 'G'),
    ('PG', 'PG'),
    ('PG-13', 'PG-13'),
    ('R', 'R'),
]


# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    rating = models.CharField(
        max_length=5,
        choices=RATING_CHOICES,
        default='G',
        help_text='MPAA-style rating used for content filtering',
    )
    def __str__(self):
        return str(self.id) + ' - ' + self.name
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name="liked_reviews", blank=True)
    reports = models.ManyToManyField(User, related_name="reported_reviews", blank=True)
    is_removed = models.BooleanField(default=False)

    def total_likes(self):
        return self.likes.count()

    def total_reports(self):
        return self.reports.count()

    def __str__(self):
        return f"{self.id} - {self.movie.name}"
