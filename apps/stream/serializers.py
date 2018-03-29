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
# from django.contrib.auth.models import User

from .models import Stream

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
    # streamer = ProfileDetailSerializer(read_only = True)
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
    # streamer = ProfileDetailSerializer(read_only = True)
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
