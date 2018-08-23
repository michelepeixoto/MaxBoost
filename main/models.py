from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=22, verbose_name='username')
    password = models.CharField(max_length=44, verbose_name='password')
    password2 = models.CharField(max_length=44, verbose_name='password2')
    email = models.EmailField(max_length=254, verbose_name='email')
    picture = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT),
                               upload_to='profile_pics',
                               default="settings.MEDIA_ROOT/profile_pics/default_profile_pic.png")
    #friends = models.CharField(max_length=800)
    is_online = models.BooleanField(default=False)
    time_online = models.FloatField(default="0.0") #amount in minutes
    game_playing = models.CharField(max_length=500, blank=True)
    is_booster = models.BooleanField()
    hire_price = models.FloatField(default="0.00")

    def __str__(self):
        return self.username

class Game(models.Model):
    title = models.CharField(max_length=80)
    picture = models.ImageField(upload_to='game_pics')

    def __str__(self):
        return self.title


class GameStat(models.Model):
    game_title = models.CharField(max_length=80)
    username = models.CharField(max_length=22)
    times_played = models.IntegerField()
    hours_played = models.DurationField()
    level = models.CharField(max_length=22)
    # wins = models.IntegerField() -> probably need game api, otherwise would have to ask user for manual input

    def __str__(self):
        return "{username}'s stats for {game_title}".format(self.username, self.game_title)


class Message(models.Model):
    sender = models.CharField(max_length=22)
    receiver = models.CharField(max_length=22)
    subject = models.CharField(max_length=40)
    content = models.CharField(max_length=600)

    def __str__(self):
        return "{sender} to {receiver}: {subject}".format(self.sender, self.receiver, self.subject)
