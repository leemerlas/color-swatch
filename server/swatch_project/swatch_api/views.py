from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets, views
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from swatch_api.serializers import RGBSwatchSerializer, HSLSwatchSerializer
from swatch_api.models import RGBSwatch, HSLSwatch

import random


class RGBSwatchViewSet(viewsets.ModelViewSet):
    queryset = RGBSwatch.objects.all()
    # randomSwatch = RGBSwatch('rgb', 100, 100, 100)
    # print(randomSwatch)
    serializer_class = RGBSwatchSerializer
    

class HSLSwatchViewSet(viewsets.ModelViewSet):
    queryset = HSLSwatch.objects.all()
    serializer_class = HSLSwatchSerializer

class SwatchView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request):

        swatch_list = []

        count = 5

        while count > 0:

            swatch_type = random.choice(['rgb', 'hsl'])
            temp_obj = {}
            
            temp_obj['swatch_type'] = swatch_type
            if (swatch_type == 'rgb'):
                temp_obj['red'] = random.randint(0,256)
                temp_obj['green'] = random.randint(0,256)
                temp_obj['blue'] = random.randint(0,256)
            else:
                temp_obj['hue'] = str(random.randint(0,360))
                temp_obj['saturation'] = str(random.randint(0,100))+'%'
                temp_obj['lightness'] = str(random.randint(0,100))+'%'

            swatch_list.append(temp_obj)
            count -= 1

        return Response({
            'swatches' : swatch_list
        })