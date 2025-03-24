from rest_framework.viewsets import ViewSet
from mypet.api.models import Lost
from mypet.api.serializers import LostSerializer
from mypet.api.services import LostService
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


class LostViewSet(ViewSet):

    def list(self, request):
        user = request.user.id
        lost_list_data = LostService.list_complete(user=user)
        return Response(lost_list_data, status=status.HTTP_200_OK)

    def create(self, request):
        user = request.user.id
        lost_data = LostService.create_complete(request.data, user)
        return Response(lost_data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        lost_data = LostService.update_complete(request.data, pk)
        return Response(lost_data, status=status.HTTP_200_OK)
