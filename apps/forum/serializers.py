from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    RelatedField,
    ReadOnlyField,
    )

from apps.forum.models import Board, Post, Thread

class BoardListSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'id',
            'name',
        ]


class BoardDetailSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'id',
            'name',
            'slug',
            'abbreviation',
            'lastUpdated'
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
    class Meta:
        board = BoardDetailSerializer(read_only=True)
        image = SerializerMethodField()
        model = Thread
        fields = [
            'title',
            'slug',
            'created',
            'creator',
            'board',
            'numberOfReplies',
            'latestReplyTime',
            'image',
            'viewCount',
            'numberOfImages'
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
            'creator',
            'board',
            'numberOfReplies',
            'image',
            'viewCount',
            'numberOfImages'
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
        thread = ThreadDetailSerializer(read_only=True)
        model = Post
        image = SerializerMethodField()
        fields = [
            'content',
            'created',
            'creator',
            'post',
            'image'
        ]

        def get_image(self,obj):
            try:
                iamge = obj.image.url
            except:
                image = None
            return image

class PostListSerializer(ModelSerializer):
    class Meta:
        thread = ThreadDetailSerializer(read_only = True)
        model = Post
        image = SerializerMethodField()
        fields = [
            'content',
            'created',
            'creator',
            'post',
            'image'
        ]
