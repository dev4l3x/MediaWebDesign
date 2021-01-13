from django.db import models
from django.utils.html import mark_safe
from adminsortable.models import Sortable


class Image(Sortable):
    class Meta(Sortable.Meta):
        pass

    source = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.source.storage, self.source.path
        # Delete the model before the file
        super(Image, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    @property
    def thumbnail_preview(self):
        if self.source:
            return mark_safe('<img src="{}" width="400" height="400" />'.format(self.source.url))
        return ""


class PortfolioImage(models.Model):
    source = models.ImageField(upload_to="portfolioimages/")
    title = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.source.storage, self.source.path
        # Delete the model before the file
        super(PortfolioImage, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    @property
    def thumbnail_preview(self):
        if self.source:
            return mark_safe('<img src="{}" width="400" height="400" />'.format(self.source.url))
        return ""
