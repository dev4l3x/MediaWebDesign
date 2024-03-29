from django.db import models
from django.utils.html import mark_safe

class Brand(models.Model):
    source = models.ImageField(upload_to="brands_logos/")
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.source.storage, self.source.path
        # Delete the model before the file
        super(Brand, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    @property
    def thumbnail_preview(self):
        if self.source:
            return mark_safe('<img src="{}" width="400" height="400" />'.format(self.source.url))
        return ""


