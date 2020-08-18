from django.db import models
from fontawesome_5.fields import IconField
from .language import Language


class Service(models.Model):
    icon = IconField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


