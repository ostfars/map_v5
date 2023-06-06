from rest_framework_gis import serializers
from gponmap.models import Point, QgisPoint, QgisLine


class PointSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id", "name")
        geo_field = "location"
        model = Point


class QgisPointSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = QgisPoint
        geo_field = 'geom'
        fields = '__all__'


class QgisLineSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = QgisLine
        geo_field = 'geom'
        fields = '__all__'
