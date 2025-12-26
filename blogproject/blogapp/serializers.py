from rest_framework import serializers

from .models import Post, Profile, Reaction

class Postserializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        #WE can keep it like this, still working. Soon need authentication for the current user
        fields = ['post_id','title','author','post', 'created_at']
        #in browsable API the user id will be displayed, need to get the name.
        read_only_fields = ['author','created_at'] #These fields are not required for input


#serializer for Profile model
class Profileserializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # WE can keep it like this, still working. Soon need authentication for the current user
        fields = ['profile_id','bio','profile_picture','user']

#serializer for Reaction model
class Reactionserializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['reaction_id','post', 'reaction']