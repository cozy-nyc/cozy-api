from rest_framework.serializers import(
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

from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Stream, Profile, Note

class NoteCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'title',
            'description',
            'uploader',
            'service',
            'link',
            'noteType'
        ]

class NoteDetailSerialzer(ModelSerializer):
    name = ReadOnlyField()
    class Meta:
        model = Note
        fields = [
            'id',
            'title',
            'description',
            'name',
            'uploader',
            'service',
            'link',
            'noteType'
        ]

class NoteListSerializer(ModelSerializer):
    name = ReadOnlyField()
    class Meta:
        model = Note
        fields = [
            'id',
            'title',
            'uploader',
            'name',
            'service',
            'noteType'
        ]


class StreamCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Stream
        fields = [
            'title',
            'description',
            'channel',
            'service',
            'live'
        ]

class StreamDetailSerializer(ModelSerializer):
    streamer = ProfileDetailSerializer(read_only = True)
    class Meta:
        model = Stream
        fields = [
            'id',
            'title',
            'description',
            'channel',
            'service',
            'live',
            'viewers',
            'featured',
            'streamer'
        ]

class StreamListSerializer(ModelSerializer):
    streamer = ProfileDetailSerializer(read_only = True)
    class Meta:
        model = Stream
        fields = [
            'id',
            'title',
            'service',
            'live',
            'viewers',
            'streamer'
        ]
