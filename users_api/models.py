from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    poster_url = models.URLField()
    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game, blank=True, related_name='wishlist_games')
    def __str__(self):
        return "User's, " + self.user.__str__() + ", wishlist."

class Favorites(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game, blank=True, related_name='favorite_games')

    def __str__(self):
        return "User's, " + self.user.__str__() + ", favorites list."

class Friends(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, blank=True, related_name="friend_list")