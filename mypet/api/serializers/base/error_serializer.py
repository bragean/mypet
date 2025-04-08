from rest_framework.serializers import (
    Serializer,
    CharField,
)


class MessageSerializer(Serializer):
    atribute = CharField(max_length=16)
    message = CharField()


class ErrorSerializer(Serializer):
    detail = CharField()
    code = CharField(max_length=32)
    messages = MessageSerializer(read_only=True, many=True)
