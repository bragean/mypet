from rest_framework.viewsets import ModelViewSet
from mypet.api.models import Lost
from mypet.api.serializers import LostSerializer
from mypet.api.services import LostService
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status


class LostViewSet(ModelViewSet):
    queryset = Lost.objects.filter(is_active=True)
    serializer_class = LostSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        user = request.user.id
        lost_list_data = LostService.list(user=user)
        return Response(lost_list_data, status=status.HTTP_200_OK)
