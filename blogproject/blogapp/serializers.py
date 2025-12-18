from rest_framework import serializers

from .models import Post

class Postserializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        #WE can keep it like this, still working. Soon need authentication for the current user
        fields = ['post_id','title','author','post', 'created_at']
        #in browsable API the user id will be displayed, need to get the name.
        read_only_fields = ['author','created_at'] #These fields are not required for input


#User registration
