from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    RelatedField,
    ReadOnlyField,
    PrimaryKeyRelatedField,
    ReadOnlyField,
    Field
    )

from apps.forum.models import Board, Post, Thread
from apps.accounts.models import Profile
from apps.accounts.serializers import ProfileDetailSerializer



class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'message',
            'poster',
            'thread',
            'image'
        ]


class PostDetailSerializer(ModelSerializer):
    poster = ProfileDetailSerializer(read_only = True)
    class Meta:
        model = Post
        image = SerializerMethodField()

        fields = [
            'id',
            'created',
            'poster',
            'message',
            'image'
        ]

        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image

class PostListSerializer(ModelSerializer):
    poster = ProfileDetailSerializer(read_only = True)
    class Meta:
        model = Post
        image = SerializerMethodField()
        fields = [
            'id',
            'created',
            'poster',
            'message',
            'image'
        ]

class ThreadCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Thread
        fields = [
            'title',
            'board',
            'image'
        ]


class ThreadDetailSerializer(ModelSerializer):
    posts = PostDetailSerializer(many = True, read_only = True)
    class Meta:
        image = SerializerMethodField()
        model = Thread
        fields = [
            'id',
            'title',
            'slug',
            'created',
            'poster',
            'tag',
            'blurb',
            'board',
            'replyCount',
            'latestReplyTime',
            'views',
            'imageCount',
            'posts'
        ]

        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image

class ThreadListSerializer(ModelSerializer):
    blurb = ReadOnlyField()
    class Meta:
        image = SerializerMethodField()
        model = Thread
        fields = [
            'id',
            'title',
            'blurb',
            'views',
            'replyCount',
            'imageCount',
            'created',
            'poster',
            
        ]

        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image


class BoardListSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'id',
            'name',
            'tag'
        ]

class BoardDetailSerializer(ModelSerializer):
    threads = ThreadListSerializer(many=True, read_only=True)
    class Meta:
        model = Board
        fields = [
            'id',
            'name',
            'slug',
            'tag',
            'threads'
        ]
class BoardCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'name',
            'tag'
        ]
