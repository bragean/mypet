from .serializers import UserSerializer, UserProfileSerializer, UserCreateSerializer
from ..models import User, UserProfile


class UserService:

    def create(data):
        user_serializer = UserCreateSerializer(data=data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return user_serializer.data

    def create_profile(data):
        user_profile_serializer = UserProfileSerializer(data=data)
        user_profile_serializer.is_valid(raise_exception=True)
        user_profile_serializer.save()
        return user_profile_serializer.data

    def create_user_with_profile(data):
        user_serializer = UserService.create(data)
        user_profile_serializer = UserService.create_profile(
            data={"user": user_serializer["id"]}
        )
        user_complete_serializer = {
            "id": user_serializer["id"],
            "name": user_serializer["name"],
            "first_name": user_serializer["first_name"],
            "last_name": user_serializer["last_name"],
            "email": user_serializer["email"],
            "profile": user_profile_serializer,
        }

        return user_complete_serializer
