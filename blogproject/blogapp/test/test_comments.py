from http.client import responses

import pytest
from django.contrib.auth.models import User
from django.template.defaultfilters import title
from django.template.defaulttags import comment
from pytest_django.fixtures import client
from rest_framework import status

from rest_framework.test import APIClient
from blogapp.models import Post, Comment, CommentReaction




@pytest.mark.django_db
def test_owner_can_delete_comment():

    # 1. CREATE A TEST USER
    user = User.objects.create_user("owner", password="pass")

    # 2. CREATE A POST because we need value from the FK
    post = Post.objects.create(title="Post",post="Body", author=user)

    # 3. CREATE A COMMENT because we need value from the FK
    comment = Comment.objects.create(comment="HI",user=user,post=post)

    # 4. INITIALIZE API CLIENT
    client = APIClient()
    client.force_authenticate(user=user)

    # 5. DELETE REQUEST
                            # <-- f-string evaluates comment.pk
    response =client.delete(f"/api/comments/{comment.pk}/") # ⚠ f-string is critical

    assert response.status_code == 204
    assert not Comment.objects.filter(pk=comment.pk).exists()

@pytest.mark.django_db
def test_owner_can_update_comment():
    """
      Test that the comment owner is allowed to update their own comment.
      """
    # Create a user who will own the comment
    user = User.objects.create_user(username="owner", password="pass")

    # Create a post owned by the same user
    #author need an FK value
    post = Post.objects.create(title="Post",post="Body", author=user)

    # Authenticate as the comment owner
    #This user and post need FK values
    comment = Comment.objects.create(
        comment="Original comment", user = user , post=post

    )

    # Authenticate as the comment owner
    client = APIClient()
    client.force_authenticate(user=user)

    # Data to update the comment
    payload = {
        "comment" :"Updated Comment"
    }

    # Send PATCH request to update the comment
    response = client.patch(
        f"/api/comments/{comment.comment_id}/",
        payload,
        format="json"
    )

    #Refresh comment from the database
    comment.refresh_from_db()

    #Assertions
    assert response.status_code == status.HTTP_200_OK
    assert  comment.comment == "Updated Comment"

@pytest.mark.django_db
def test_user_can_react_to_comment():
    """
       PURPOSE:
       Ensure an authenticated user can create a reaction
       for a specific comment.
       """
    #Create user
    user = User.objects.create_user(username="testuser", password="pass123")

    #Create post and comment for FK values
    post = Post.objects.create(title="post",post="body", author = user)
    comment = Comment.objects.create(comment="Nice Post", post=post, user=user)

    #Authenticate client
    client = APIClient()
    client.force_authenticate(user=user)

    # Payload for reaction
    # Payload sent to the API containing the comment ID and the selected reaction
    payload = {
        "comment" : comment.comment_id,        # ID of the comment that the user is reacting to
        "reaction": "haha",                         # The reaction type chosen by the user
    }

    #Call the API
    # Send a POST request to the react-comment endpoint using the authenticated client
    response = client.post('/react-comment/', payload, format="json")

    #Assertions
    # Assert that the API request was successful (reaction was accepted)
    assert  response.status_code == status.HTTP_200_OK

    # Assert that exactly one CommentReaction record was created in the database
    assert CommentReaction.objects.count() == 1

    # Retrieve the first (and only) reaction object from the database
    reaction = CommentReaction.objects.first()
    # Assert that the stored reaction value matches the expected reaction ("haha")
    assert reaction.reaction == "haha"
