from django.db import models
from django.contrib.auth.models import User

RATING_CHOICES = [
    ('G', 'G'),
    ('PG', 'PG'),
    ('PG-13', 'PG-13'),
    ('R', 'R'),
]

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    max_content_rating = models.CharField(
        max_length=5,
        choices=RATING_CHOICES,
        default='R',
        help_text='Highest rating of content you want to see',
    )

    def __str__(self):
        return f"Profile for {self.user.username}"
