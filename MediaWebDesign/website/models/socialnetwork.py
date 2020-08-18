from django.db import models
from fontawesome_5.fields import IconField


class SocialNetwork(models.Model):
    title = models.CharField(max_length=50)
    icon = IconField()
    link = models.CharField(max_length=400, default="")

    def __str__(self):
        return self.title

