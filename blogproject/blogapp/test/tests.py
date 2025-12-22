import tempfile
from http.client import responses

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from pytest_django.fixtures import client
from rest_framework.test import APIClient
from PIL import Image

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

