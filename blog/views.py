from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated

from blog.serializers import *


class PostLikesCreate(CreateAPIView):
    serializer_class = LikePostSerializer
    queryset = PostLikes.objects.all()


class PostLikesList(ListAPIView):
    serializer_class = LikePostSerializer
    queryset = PostLikes.objects.all()
    permission_classes = (IsAuthenticated)


class PostLikesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = LikePostSerializer
    queryset = PostLikes.objects.all()


class PostCreate(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostList(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentCreate(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentList(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostDetail(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentDetail(RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostLikesDetail(RetrieveAPIView):
    serializer_class = LikePostSerializer
    queryset = PostLikes.objects.all()


