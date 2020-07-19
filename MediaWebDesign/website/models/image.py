from django.db import models


class Image(models.Model):
    source = models.ImageField(upload_to="images/")
    include_portfolio = models.BooleanField(default=False)
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
