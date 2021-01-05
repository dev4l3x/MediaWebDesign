from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=250, default="")
    reason = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name




