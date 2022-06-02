from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import User, Group, Post, Comment, Follow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        ref_name = 'ReadOnlyUsers'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date',
                  'author', 'image', 'group')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        read_only=True)
    author = serializers.StringRelatedField(
        read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        slug_field='username',
        required=False,
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username')

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=['user', 'following']
            )
        ]

    def validate(self, data):
        if self.context.get('request').user == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписатся на самого себя!')
        return data
