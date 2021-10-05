from django.db import models


class PageInfo(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)

    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
