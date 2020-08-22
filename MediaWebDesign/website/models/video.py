from django.db import models
from .language import Language


class Video(models.Model):
    title = models.CharField(max_length=100, default="")
    link = models.CharField(max_length=600, default="")

    def __str__(self):
        return self.title


class VideoTranslate(models.Model):

    class Meta:
        unique_together = (('video', 'language'),)

    video = models.ForeignKey(Video, on_delete=models.CASCADE, default=None)
    title_translated = models.CharField(max_length=100, default="")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "{0} - {1}".format(self.video.title, self.language)


