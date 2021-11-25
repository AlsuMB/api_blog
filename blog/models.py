from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


# def articles(self):
#     return self.get_queryset().filter(content_type__model='post').order_by('-post__pub_date')
#
#
# def comments(self):
#     return self.get_queryset().filter(content_type__model='comment').order_by('-comments__pub_date')


User = get_user_model()


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(null=False)
    image = models.ImageField(upload_to='blog/%Y/%m/%d')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()


class PostLikes(models.Model):
    like_users = models.ManyToManyField(User)
    like_post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,related_name='likepost')
    like_comment = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,related_name='likecomment')
