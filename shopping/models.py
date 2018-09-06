from django.db import models

# Create your models here.
class ShoppingItem(models.Model):
    name = models.CharField(max_length=60)
    quantity = models.PositiveSmallIntegerField(default=1)
    checked = models.BooleanField(default=False)
