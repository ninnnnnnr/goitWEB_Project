from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """
    Stores a single note entry
    """
    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # author is taken from authenticated user

    def __str__(self):
        return f'"{self.title}"'
