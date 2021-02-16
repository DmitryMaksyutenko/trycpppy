from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    """Model contains authors information."""

    author_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=132, null=True)
    social = models.CharField(max_length=132, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
