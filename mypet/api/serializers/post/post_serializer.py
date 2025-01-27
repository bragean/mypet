from mypet.api.models import Post, PostImage
from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]


class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]
