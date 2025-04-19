from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255)
    github_link = models.URLField(blank=True)
    connections = models.ManyToManyField('self', symmetrical=False, related_name='connected_to', blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
