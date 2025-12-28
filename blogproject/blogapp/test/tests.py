import tempfile
from enum import verify
from http.client import responses

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from pytest_django.fixtures import client
from rest_framework.test import APIClient
from PIL import Image
from blogapp.models import Post, Comment


# Mark this test as requiring database access
@pytest.mark.django_db
def test_create_profile_with_image():
    # create temporary image file
    # Create a 100x100 RGB image in memory (no real file needed)
    image = Image.new("RGB", (100, 100))

    # Create a temporary file on disk to save the image
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")

    # Save the image to the temporary file in JPEG format
    image.save(tmp_file, format="JPEG")
    # Move file pointer back to the beginning so it can be read later
    tmp_file.seek(0)

    #create a test user
    #create_user() is built-in
    # Django built-in method to create a new user in the test database
    user = User.objects.create_user(

        username = "testusername",
        password = "testpassword"
    )

    # #  Authenticate user
    # DRF's APIClient allows us to make requests like a real user
    client = APIClient()
    # Force authentication to simulate a logged-in user without login requests
    client.force_authenticate(user=user)

    # Prepare image upload
    # SimpleUploadedFile mimics an uploaded file (like from a browser)
    uploaded_image = SimpleUploadedFile(
        name="test.jpg",                 # Filename
        content = tmp_file.read(),      # Read the content of the temporary imag
        content_type="image/jpeg"       # MIME type

    )

    # Send POST request
    # Hardcoded URL for testing; could use reverse('profile-create') for safety
    response = client.post(
        "/api/profiles/",   # Endpoint to test
        {
            "bio": "This is my bio",        # Example bio data
            "profile_picture": uploaded_image       # Uploading the image
        },
        format="multipart"      # Required to handle file uploads
    )

    #Assertions
    # Check if the HTTP response status code is 201 Created
    assert response.status_code == 201

    # Check that the bio in the response matches the data sent
    assert response.data["bio"] == "This is my bio"

    # Check that the profile_picture field exists in the response
    assert "profile_picture" in response.data




@pytest.mark.django_db
def test_create_comment_api():
    # -------------------------------
    # 1. CREATE A TEST USER
    # -------------------------------
    # This user will be used to:
    # - authenticate the API request
    # - become the owner (FK) of the comment
    # Tests must create their own users to stay isolated.
    user = User.objects.create_user(
        username="testuser",
        password="testpassword"
    )

    # -------------------------------
    # 2. CREATE A POST (PARENT OBJECT)
    # -------------------------------
    # A Comment cannot exist without a Post.
    # We create a Post first so the FK constraint is valid.
    # Field names MUST match the Post model exactly.
    post = Post.objects.create(
        title="Test Post",
        post="Post content",
        author=user
    )
    # -------------------------------
    # 3. INITIALIZE THE API CLIENT
    # -------------------------------
    # APIClient simulates a real HTTP client (like Postman).
    client = APIClient()
    # -------------------------------
    # 4. AUTHENTICATE THE REQUEST
    # -------------------------------
    # force_authenticate bypasses the login flow
    # and directly attaches `user` to request.user.
    # Required because the endpoint uses IsAuthenticated.
    client.force_authenticate(user=user)

    # -------------------------------
    # 5. SEND POST REQUEST TO CREATE COMMENT
    # -------------------------------
    # We send only the fields that the client is allowed to send.
    # The `user` field is NOT included because it is set
    # automatically in the view using request.user.
    response = client.post("/api/comments/", {
        "comment": "This is the comments sample",
        "post": post.post_id   # or post.id
    })

    # -------------------------------
    # 6. API RESPONSE ASSERTIONS
    # -------------------------------
    # These assertions verify that:
    # - the request succeeded
    # - the API returned correct data
    assert response.status_code == 201
    assert response.data["comment"] == "This is the comments sample"
    assert response.data["post"] == post.post_id
    assert response.data["user"] == user.id

    # DB assertions (VERY IMPORTANT)
    # -------------------------------
    # 7. DATABASE ASSERTIONS (CRITICAL)
    # -------------------------------
    # API tests should ALSO verify the database state,
    # not just the response.
    comment = Comment.objects.first()

    # Ensure the object was actually saved
    assert comment is not None

    # Verify correct field values and FK relationships
    assert comment.comment == "This is the comments sample"
    assert comment.post == post
    assert comment.user == user


