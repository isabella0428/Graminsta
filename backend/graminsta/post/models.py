"""
Here defines the database tables for post app
"""

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post Table
    """
    postId = models.IntegerField(default=0)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="Publisher_Of_Post")
    time = models.DateTimeField(auto_now=True)
    markedUser = models.ManyToManyField(
        User, related_name="User_Who_Marked_Post")
    content = models.BinaryField()


class Comment(models.Model):
    """
    Comment Table
    """
    commentId = models.IntegerField(default=0)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
