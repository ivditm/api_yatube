from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly
from posts.models import Comment, Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def find_post(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        return post

    def get_queryset(self):
        post = self.find_post()
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post = self.find_post()
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
