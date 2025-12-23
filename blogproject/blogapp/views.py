

from rest_framework.views import APIView
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from  rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from rest_framework import viewsets,permissions

#for the the current User
from rest_framework.permissions import IsAuthenticated, AllowAny

#import the models here
from .models import Post, Profile
#import the Serializers
from .serializers import Postserializers, Profileserializers

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
