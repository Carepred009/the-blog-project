from django.template.defaulttags import comment
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
    # Computed field used by the frontend to decide
    # whether the delete button should be shown
    is_owner = serializers.SerializerMethodField()

    # Expose user ID explicitly without allowing edits
    user_id = serializers.IntegerField(source="user.id", read_only=True)

    # Expose username so Vue does not need another API call
    username = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Comment
        fields = [
            "comment_id",
            "comment",
            "user_id",
            "username",
            "post",
            "user",
            "created_at",
            "is_owner",
        ] # add this user if you didnt use the self.user in the view
        #read_only_fields = ["user"]

    # Determines whether the currently authenticated user
    # is the owner of this comment.
    # Used ONLY for frontend logic (UI), not for security.
    def get_is_owner(self, obj):
        request = self.context.get("request")
        # Ensure request exists and user is authenticated
        if request and request.user.is_authenticated:
            return obj.user == request.user
        return False

#serializer for Reaction model
class PostReactionserializer(serializers.ModelSerializer):
    class Meta:
        model = PostReaction
        fields = ['reaction_id','post', 'reaction']


class CommentReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReaction
        fields = ['reaction_id', 'comment','reaction']

'''
class CommentReactSerializer(serializers.ModelSerializer):

    #Exposes the comment where the user is reacting and what reaction
    comments = serializers.CharField(source="comment.comment", read_only=True)
    class Meta:
        model = CommentReaction
        fields = ['reaction_id', 'user','comment','comments','reaction']
'''
#Serializer for comment reaction
