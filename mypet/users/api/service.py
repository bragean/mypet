from .serializers import UserSerializer, UserProfile, UserCreateSerializer
from ..models import User, UserProfile


class UserService:

    def create(data):
        user_serializer = UserCreateSerializer(data=data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return user_serializer.data
    
    def create_profile(data):
        user_profile_serializer = UserProfile(data=data)
        user_profile_serializer.is_valid(raise_exception=True)
        user_profile_serializer.save()
        return user_profile_serializer.data