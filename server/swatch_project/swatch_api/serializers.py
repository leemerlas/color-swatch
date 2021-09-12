from rest_framework import serializers
from swatch_api.models import RGBSwatch, HSLSwatch

class RGBSwatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = RGBSwatch
        fields = ('swatch_type', 'red', 'green', 'blue')

class HSLSwatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSLSwatch
        fields = ('swatch_type', 'hue', 'saturation', 'brightness')

# class SwatchSerializer(serializers.ModelSerializer):
#     class Meta:
        