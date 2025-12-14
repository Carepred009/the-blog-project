from django.shortcuts import render
from rest_framework import viewsets
#for the the current User
from rest_framework.permissions import IsAuthenticated, AllowAny

#import the models here
from .models import Post
#import the Serializers
from .serializers import Postserializers

# Create your views here.
#We will use viewset for all the CRUD operation
#this view is for Post model
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-post_id') #the .order_by('-post_id') will responsible for displaying the lates posting
    serializer_class = Postserializers

        #use this to avoid anonymouse user, we wont use this for now.
        #this is needed when the user is actually log in

    #do not use any authentication when testing the basic CRUD
    #permission_classes =  [AllowAny]#[IsAuthenticated]

    #We will not us this for now, we can keep it but it will be null

   # def perform_create(self, serializer):
        #Set automatically set the author to the current logged-in user
     #   serializer.save(author = self.request.user)