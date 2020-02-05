from django.db import models
from django.conf import settings


class Item(models.Model):
    slug = models.SlugField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=120)
    quality = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    buy_price = models.IntegerField(default=0)

    def __str__(self):
        return str(self.owner.username)

# Create your models here.
