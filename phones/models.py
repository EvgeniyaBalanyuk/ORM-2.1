from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60, default=None)
    image = models.URLField(default=None)
    price = models.IntegerField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.SlugField(default=None)
