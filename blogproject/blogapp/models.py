from django.db import models

#import the user from the User model in the Django admin
from django.contrib.auth.models import User
from django.utils.translation.template import blankout


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


#Profile page for the user
class Profile(models.Model):
    profile_id = models.AutoField(primary_key = True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_images/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null =True )

    def __str__(self):
        return  self.user.username




#Comment model
class Comment(models.Model):
    comment_id = models.AutoField(primary_key = True)
    comment = models.TextField(blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name="posts")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user")
    created_at = models.DateTimeField(auto_now_add=True)  #set True for auto set the tinme with the current time

    def __str__(self):
        return self.comment

#Reaction model
class PostReaction(models.Model):
    reaction_id = models.AutoField(primary_key = True)

    REACTION_CHOICES = [
        ('like','Like'),  #like - stored in the database , Like - human-readable label (used in admin, forms, serializers)
        ('love','Love'),
        ('haha', 'Haha'),
        ('angry','Angry'),
        ('sad', 'Sad'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True , related_name='reactions')
    reaction = models.CharField(max_length=20, choices=REACTION_CHOICES)  #reaction field

    class Meta:
        unique_together = ('user', 'post') # One reaction per user per post

    def __str__(self):
        return self.reaction

class CommentReaction(models.Model):
      reaction_id = models.AutoField(primary_key=True)

      REACTION_CHOICES = [
          ('like', 'Like'),
          # like - stored in the database , Like - human-readable label (used in admin, forms, serializers)
          ('love', 'Love'),
          ('haha', 'Haha'),
          ('angry', 'Angry'),
          ('sad', 'Sad'),
      ]
      user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
      comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='reactions')
      reaction = models.CharField(max_length=20, choices=REACTION_CHOICES)  # reaction field

      class Meta:
          unique_together = ('user', 'comment')  # One reaction per user per comment

      def __str__(self):
          return self.reaction