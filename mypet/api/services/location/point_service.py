from mypet.api.serializers import PointSerializer
from mypet.api.models import Point


class PointService:

    def get(id):
        point_instance = Point.objects.get(id=id)
        point_serializer = PointSerializer(point_instance)
        return point_serializer.data

    def create(data):
        point_serializer = PointSerializer(data=data)
        point_serializer.is_valid(raise_exception=True)
        point_serializer.save()
        return point_serializer.data

    def update(data, id):
        point_instance = Point.objects.get(id=id)
        point_serializer = PointSerializer(point_instance, data=data, partial=True)
        point_serializer.is_valid(raise_exception=True)
        point_serializer.save()
        return point_serializer.data
