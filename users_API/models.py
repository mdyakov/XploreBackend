from django.db import models
from django.contrib.auth.models import User

# First model for USER.
class Game(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # needs to be reworked!!!!! games have incorrect way of binding. Needs to be a list.
    games = models.ManyToManyField(Game)
    def __str__(self):
        return "User's, " + self.user.__str__() + ", wishlist."
