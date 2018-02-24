from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    RelatedField,
    ReadOnlyField,
    PrimaryKeyRelatedField
    )

from apps.forum.models import Board, Post, Thread

class BoardListSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'id',
            'name',
            'tag'
        ]

class BoardDetailSerializer(ModelSerializer):
    threads = PrimaryKeyRelatedField(many=True, read_only=True)
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

class ThreadCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Thread
        fields = [
            'title',
            'board',
            'image'
        ]


class ThreadDetailSerializer(ModelSerializer):
    post = PrimaryKeyRelatedField(many = True, read_only = True)
    class Meta:
        board = BoardDetailSerializer(read_only=True)
        image = SerializerMethodField()
        model = Thread
        fields = [
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
    class Meta:
        board = BoardDetailSerializer(read_only=True)
        image = SerializerMethodField()
        model = Thread
        fields = [
            'title',
            'created',
            'tag',
            'poster',
            'board',
            'blurb',
            'replyCount',
            'image',
            'views',
            'imageCount'
        ]

        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'post',
            'content',
            'thread',
            'image'
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        image = SerializerMethodField()
        fields = [
            'content',
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
    class Meta:
        model = Post
        image = SerializerMethodField()
        fields = [
            'content',
            'created',
            'poster',
            'message',
            'image'
        ]
