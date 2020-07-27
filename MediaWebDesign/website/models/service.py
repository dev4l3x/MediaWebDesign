from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


