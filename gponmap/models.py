from django.contrib.gis.db import models


class Point(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        return self.name


class QgisPoints(models.Model):
    geom = models.PointField()

    def __str__(self):
        return self.geom

    class Meta:
        managed = False
        db_table = 'points_all'


class QgisPoint(models.Model):
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'points_all'


class QgisLine(models.Model):
    geom = models.MultiLineStringField()

    class Meta:
        managed = False
        db_table = 'lines_all'
