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

    def get_with_profile(id):
        user_instance = UserService.get(id=id)
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

        return user_serializer

    def update(id, data):
        user_instance = User.objects.get(id=id)
        user_serializer = UserCreateSerializer(user_instance, data=data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return user_serializer.data

    def update_profile(id, data):
        user_profile_instance = UserProfile.objects.get(user=id)
        user_serializer = UserProfileSerializer(
            user_profile_instance, data=data, partial=True
        )
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return user_serializer.data

    def update_with_profile(id, data):
        user_serializer = UserService.update(id=id, data=data)
        user_profile_serializer = UserService.update_profile(
            id=id, data=data["profile"]
        )
        user_serializer = {
            "id": user_serializer["id"],
            "name": user_serializer["name"],
            "first_name": user_serializer["first_name"],
            "last_name": user_serializer["last_name"],
            "email": user_serializer["email"],
            "profile": user_profile_serializer,
        }

        return user_serializer

    def exists(id):
        return User.objects.filter(id=id, is_active=True).exists()

    def get(id):
        return User.objects.get(id=id)
