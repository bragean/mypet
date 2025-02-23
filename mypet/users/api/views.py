from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.permissions import AllowAny

from mypet.users.models import User, UserProfile

from .serializers import UserSerializer, UserProfileSerializer
from .service import UserService


class UserViewSet(ViewSet):

    @action(detail=False)
    def me(self, request):
        user_serializer = UserService.get_with_profile(request.user.id)
        return Response(user_serializer, status=status.HTTP_200_OK)

    @action(detail=False, methods=["put"])
    def update_profile(self, request):
        user_serializer = UserService.update_with_profile(
            id=request.user.id, data=request.data
        )
        return Response(user_serializer, status=status.HTTP_200_OK)


class UserPublicViewSet(ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        user = UserService.create_user_with_profile(data=request.data)
        return Response(user, status=status.HTTP_201_CREATED)
