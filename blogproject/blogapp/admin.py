from django.contrib import admin

#import the model to register to the Djago admin
from .models import Post, Profile
# Register your models here.

admin.site.register(Post)
admin.site.register(Profile)

