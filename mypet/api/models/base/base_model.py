import uuid

from django.db.models import Model
from django.db.models import DateField, UUIDField, BooleanField


class Base(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = DateField(auto_now_add=True)
    modified = DateField(auto_now=True)
    created_by = UUIDField(editable=False, null=True)
    modified_by = UUIDField(editable=False, null=True)
    is_active = BooleanField(default=True)

    class Meta:
        abstract = True
