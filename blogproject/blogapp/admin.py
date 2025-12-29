from django.contrib import admin

#import the model to register to the Djago admin
from .models import Post, Profile, PostReaction, CommentReaction, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(PostReaction)
admin.site.register(CommentReaction)
admin.site.register(Comment)

