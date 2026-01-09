from http.client import responses

import pytest
from django.contrib.auth.models import User


from rest_framework.test import APIClient
from blogapp.models import Post, Comment

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