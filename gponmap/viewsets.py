from rest_framework import viewsets
from rest_framework_gis import filters

from gponmap.models import Point, QgisPoints
from gponmap.serializers import PointSerializer, QgisPointSerializer


class PointViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class QgisPointViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = "geom"
    filter_backends = (filters.InBBoxFilter,)
    queryset = QgisPoints.objects.all()
    serializer_class = QgisPointSerializer
