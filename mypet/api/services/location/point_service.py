from mypet.api.serializers import PointSerializer


class PointService:

    def create(data):
        point_serializer = PointSerializer(data=data)
        point_serializer.is_valid(raise_exception=True)
        point_serializer.save()
        return point_serializer.data
