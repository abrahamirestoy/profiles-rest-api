from django.contrib import admin
#Apartado 7.26
from profiles_api import models

#Apartado 7.26
admin.site.register(models.UserProfile)

#Apartado 12.59
admin.site.register(models.ProfileFeedItem)
