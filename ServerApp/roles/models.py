from django.db import models
from django.contrib.auth.models import User


class Authors(models.Model):
    """Model contains authors information."""

    class Meta:
        verbose_name = "Authors"
        verbose_name_plural = "Authors"

    author_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=132, null=True, blank=True)
    social = models.CharField(max_length=132, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        user = User.objects.get(pk=self.user_id.id)
        return user.username
