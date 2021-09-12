from django.db import models



class RGBSwatch(models.Model):
    swatch_type = models.CharField(max_length=10)
    red = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)

class HSLSwatch(models.Model):
    swatch_type = models.CharField(max_length=10)
    hue = models.CharField(max_length=10)
    saturation = models.CharField(max_length=10)
    lightness = models.CharField(max_length=10)

