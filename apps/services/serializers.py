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
from rest_framework import serializers
from apps.services.models import Service, ServiceMessage


class ServiceMessageDetailSerializer(ModelSerializer):
    class Meta:
        model = ServiceMessage
        fields = [
            'important',
            'text'
        ]



class ServiceListSerializer(ModelSerializer):
    message = ServiceMessageDetailSerializer(read_only = True)
    class Meta:
        model = Service
        fields = [
            'service',
            'status',
            'message'
        ]


class ServiceDetailSerializer(ModelSerializer):
    message = ServiceMessageDetailSerializer(read_only = True)
    class Meta:
        model = Service
        fields = [
            'service',
            'status',
            'message'
        ]
