from django.db import models

#import the user from the User model in the Django admin
from django.contrib.auth.models import User
# Create your models here.




class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=255, null=True, blank=True)
    post = models.TextField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', blank=True, null=True) #It's at Foreign Key
    created_at = models.DateTimeField(auto_now_add=True) #set True for auto set the tinme with the current time

    #This will be use to retrieve from this model
    def __str__(self):
        return self.title

