from rest_framework_gis import serializers
from gponmap.models import Point


class PointSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id", "name")
        geo_field = "location"
        model = Point
