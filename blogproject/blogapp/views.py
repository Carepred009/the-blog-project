from django.contrib.auth.models import AnonymousUser
from rest_framework.views import APIView
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from  rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework import status



#for the the current User
from rest_framework.permissions import IsAuthenticated, AllowAny
from urllib3 import request

#import the models here
from .models import Post, Profile, Reaction
#import the Serializers
from .serializers import Postserializers, Profileserializers, Reactionserializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from .pagination import PostPagination # this is from pagination.py


# Create your views here.
#We will use viewset for all the CRUD operation
#this view is for Post model
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() #.order_by('-post_id') #the .order_by('-post_id') will responsible for displaying the lates posting
    serializer_class = Postserializers


    pagination_class = PostPagination                       # Connects pagination to this API


    filter_backends = [OrderingFilter]                      # Enables ordering via query params

    ordering_fields = ['post','author','created_at']         # Fields allowed to be ordered


    ordering = ['-post_id']                                     # Default ordering (newest first)  we can use it later




        #use this to avoid anonymouse user, we wont use this for now.
        #this is needed when the user is actually log in

    #do not use any authentication when testing the basic CRUD
    #permission_classes =  [AllowAny]#[IsAuthenticated]

    #We will not us this for now, we can keep it but it will be null

   # def perform_create(self, serializer):
        #Set automatically set the author to the current logged-in user
     #   serializer.save(author = self.request.user)


#This view is for logout to invalidates the refresh token after log out
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()

        return Response({"detail": "Logged out successfully"})


#We will use viewset for all the CRUD operation
class ProfileViewSet(viewsets.ModelViewSet):
    #queryset = Profile.objects.all() --remove this because we will link the profile to the only one user
    serializer_class = Profileserializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return ONLY the logged-in user's profile
        return Profile.objects.filter(user = self.request.user)




class ReactionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post')
        reaction_type = request.data.get('reaction')

        reaction, created = Reaction.objects.update_or_create(
            user=request.user,
            post_id=post_id,
            defaults={'reaction': reaction_type}
        )

        serializer = Reactionserializer(reaction)
        return Response(serializer.data, status=status.HTTP_200_OK)