from rest_framework import serializers

from blog.models import *


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'