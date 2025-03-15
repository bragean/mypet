from rest_framework.viewsets import ModelViewSet
from mypet.api.models import Sighting
from mypet.api.serializers import SightingSerializer
from rest_framework.permissions import IsAuthenticated


class SightingViewSet(ModelViewSet):
    queryset = Sighting.objects.filter(is_active=True)
    serializer_class = SightingSerializer
    permission_classes = [IsAuthenticated]
