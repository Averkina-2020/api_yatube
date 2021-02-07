from rest_framework import serializers
from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        fields = ('text', 'author', 'pub_date', 'image', 'id')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        model = Comment
