from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.generics import ListAPIView
from .models import QgisPoint, QgisLine
from .serializers import QgisPointSerializer, QgisLineSerializer


class GponmapView(TemplateView):
    template_name = "map.html"


class QgisMapView(TemplateView):
    template_name = "qgis_test.html"


class QgisPointAPIView(ListAPIView):
    queryset = QgisPoint.objects.all()
    serializer_class = QgisPointSerializer


class QgisLineAPIView(ListAPIView):
    queryset = QgisLine.objects.all()
    serializer_class = QgisLineSerializer
