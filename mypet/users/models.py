from typing import ClassVar
import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ForeignKey, OneToOneField, UUIDField
from django.db.models import EmailField, CASCADE, BooleanField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for mypet.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    id = UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(_("First Name of User"), blank=True, max_length=255)
    last_name = CharField(_("Last Name of User"), blank=True, max_length=255)
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore[assignment]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


class UserProfile(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = OneToOneField(User, on_delete=CASCADE)
    identifier = CharField(max_length=15)
    address = CharField(max_length=255, blank=True)
    phone = CharField(max_length=15)
    image = ImageField(upload_to="user_profile/", null=True, blank=True)
    is_phone_verified = BooleanField(default=False)
    is_email_verified = BooleanField(default=False)
