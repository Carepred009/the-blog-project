from django.contrib import admin

#import the model to register to the Djago admin
from .models import Post
# Register your models here.

admin.site.register(Post)

