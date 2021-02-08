from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Post
from .serializers import CommentSerializer, PostSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        comments = post.comments
        return comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
