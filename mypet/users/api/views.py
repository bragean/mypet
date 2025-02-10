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


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        pass

    @action(detail=False)
    def me(self, request):
        user_instance = User.objects.filter(
            id=self.request.user.id, is_active=True
        ).first()
        user_profile_instance = UserProfile.objects.get(user=user_instance.id)
        user_profile_serializer = UserProfileSerializer(user_profile_instance)
        user_serializer = {
            "id": user_instance.id,
            "name": user_instance.name,
            "first_name": user_instance.first_name,
            "last_name": user_instance.last_name,
            "email": user_instance.email,
            "profile": user_profile_serializer.data,
        }

        return Response(user_serializer, status=status.HTTP_200_OK)


class UserPublicViewSet(ViewSet):
    permission_classes  = [AllowAny]

    def create(self, request):
        user = UserService.create(data=request.data)
        return Response(user, status=status.HTTP_201_CREATED)
