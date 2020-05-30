from django.contrib import admin
from .models import Wishlist, Favorites, Game, Friends, ProfilePicture

admin.site.register(Wishlist)
admin.site.register(Favorites)
admin.site.register(Game)
admin.site.register(Friends)
admin.site.register(ProfilePicture)