from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    CharField,
    UUIDField,
    EmailField,
    PrimaryKeyRelatedField,
)

from mypet.users.models import User, UserProfile


class UserProfileSerializer(ModelSerializer[UserProfile]):
    class Meta:
        model = UserProfile
        exclude = ["is_email_verified", "is_phone_verified"]


class UserSerializer(Serializer):
    id = UUIDField(read_only=True)
    name = CharField(max_length=255, allow_blank=True)
    first_name = CharField(max_length=255, allow_blank=True)
    last_name = CharField(max_length=255, allow_blank=True)
    email = EmailField()
    profile = UserProfileSerializer(read_only=True)


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
            "user_permissions",
            "groups",
        ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.is_active = True
        user.save()
        return user


"""
class UserSerializer(serializers.ModelSerializer[User]):
    profile = UserProfileSerializer
    class Meta:
        model = User
        fields = ["id", "name", "email", "first_name", "second_name"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }
"""
