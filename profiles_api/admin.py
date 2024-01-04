from django.contrib import admin

from profiles_api import models

admin.site.register(models.UserProfile)             # TELLS DJANGO ADMIN TO REGISTER OUR USER PROFILE MODEL WITH THE ADMIN SITE (ACCESSIBLE FROM THE ADMIN INTERFACE)
admin.site.register(models.ProfileFeedItem)