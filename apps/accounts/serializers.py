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
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.models import User
from apps.accounts.models import Profile, Service, ServiceMessage
from django.contrib.auth.models import User
from rest_auth.models import TokenModel


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




class ProfileCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'username',
            'profileImg',
            'location'
            'bio'
        ]

class ProfileDetailSerializer(ModelSerializer):
    username = ReadOnlyField()
    lookup_field = 'user__username'

    class Meta:
        model = Profile
        image = SerializerMethodField()
        fields = [
            'id',
            'username',
            'profileImg',
            'location'
            'bio'
        ]

        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image

class ProfileListSerializer(ModelSerializer):
    username = ReadOnlyField()
    class Meta:
        model = Profile
        image = SerializerMethodField()
        fields = [
            'id',
            'username',
            'profileImg'
        ]

        def get_image(self, obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileDetailSerializer(read_only = True)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile')
