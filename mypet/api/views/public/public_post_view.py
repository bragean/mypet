from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.permissions import AllowAny
from mypet.api.services import LostService


class PublicPostViewSet(ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        start = request.query_params.get("start", None)
        end = request.query_params.get("end", None)
        lost_list_data = LostService.list_all(int(start), int(end))
        return Response(lost_list_data, status=status.HTTP_200_OK)
