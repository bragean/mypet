from rest_framework.viewsets import ModelViewSet
from mypet.api.models import Post, PostImage
from mypet.api.serializers import PostSerializer, PostImageSerializer
from rest_framework.permissions import IsAuthenticated


class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostImageViewSet(ModelViewSet):
    queryset = PostImage.objects.filter(is_active=True)
    serializer_class = PostImageSerializer
    permission_classes = [IsAuthenticated]
