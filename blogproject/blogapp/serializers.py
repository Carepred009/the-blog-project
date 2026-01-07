from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post, Profile, PostReaction, CommentReaction, Comment


class Postserializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        #WE can keep it like this, still working. Soon need authentication for the current user
        fields = ['post_id','title','author','post', 'created_at']
        #in browsable API the user id will be displayed, need to get the name.
        read_only_fields = ['author','created_at'] #These fields are not required for input


"""
    Serializer for the built-in Django User model.
    This is used to expose basic user information
    without revealing sensitive fields such as passwords.
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']


#serializer for Profile model
class Profileserializers(serializers.ModelSerializer):

    # Nested serializer for the related User (ForeignKey)
    # read_only=True ensures the user cannot be changed via the profile API
    user = UserSerializer(read_only=True)  # Nested serializer for the FK

    class Meta:
        model = Profile
        # WE can keep it like this, still working. Soon need authentication for the current user
        fields = ['profile_id','bio','profile_picture','user']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        # Read-only username instead of full user object
        user = serializers.ReadOnlyField(source="user.username")
        model = Comment
        fields = ['comment_id','comment','post', 'user'] # add this user if you didnt use the self.user in the view
        #read_only_fields = ["user"]
#serializer for Reaction model
class PostReactionserializer(serializers.ModelSerializer):
    class Meta:
        model = PostReaction
        fields = ['reaction_id','post', 'reaction']


class CommentReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReaction
        fields = ['reaction_id','comment','reaction']