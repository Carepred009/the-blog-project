from django.db import models

# Create your models here.




class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    post = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) #set True for auto set the tinme with the current time

