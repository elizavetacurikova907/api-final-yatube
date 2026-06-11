from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework.relations import SlugRelatedField
from rest_framework.response import Response
from rest_framework.serializers import (
    ImageField, ModelSerializer,
    PrimaryKeyRelatedField, SerializerMethodField, SlugRelatedField
)


from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class GroupSerializer(ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = ImageField(required=False)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = Post


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(ModelSerializer):

    user = SlugRelatedField(
        read_only=True, slug_field='username')
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, data):
        following_username = data['following']
        user = self.context['request'].user

        if not User.objects.filter(username=following_username).exists():
            raise serializers.ValidationError('Пользователь не найден.')

        following = User.objects.get(username=following_username)
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError('Подписка уже существует.')
        
        if following == user:
            raise serializers.ValidationError(
                'Невозможно оформить подписку на самого себя.')
        return data

    # def get_following(self, obj):
    #     if self.is_valid():
    #         clean_following_name = self.validated_data['following']
    #     if not User.objects.get(username=clean_following_name):
    #         return Response(
    #             {'detail': 'Пользователь не найден.'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     following = User.objects.get(username=clean_following_name)
    #     user = self.request.user
    #     if Follow.objects.filter(user=user, following=following).exists():
    #         return Response(
    #             {'detail': 'Подписка уже существует.'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     return following
