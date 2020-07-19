from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100, default="")
    is_url = models.BooleanField(default=False)
    content = models.CharField(max_length=600, default="")

    def __str__(self):
        return self.title
