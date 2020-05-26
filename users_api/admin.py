from django.contrib import admin
from .models import Wishlist, Favorites, Game

admin.site.register(Wishlist)
admin.site.register(Favorites)
admin.site.register(Game)