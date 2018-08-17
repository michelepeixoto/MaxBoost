from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=22, verbose_name='username')
    password = models.CharField(max_length=44, verbose_name='password')
    email = models.EmailField(max_length=254, verbose_name='email')
    #friends = models.CharField(max_length=800)
    games_played = models.CharField(max_length=500, blank=True)
    is_online = models.BooleanField(default=False)
    hire_price = models.FloatField(default="0.00")
    time_online = models.FloatField(default="0.0") #amount in minutes
    picture = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT),
                               upload_to='profile_pics',
                               default="settings.MEDIA_ROOT/profile_pics/default_profile_pic.png")

    def __str__(self):
        return self.username

class Game(models.Model):
    title = models.CharField(max_length=80)
    picture = models.ImageField(upload_to='game_pics')

    def __str__(self):
        return self.title