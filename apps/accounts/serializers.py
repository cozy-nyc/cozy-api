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
from apps.accounts.models import Profile, Clan, ProfileImg


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


class ProfileCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'clan',
            'profileImg',
            'location'
        ]

class ProfileDetailSerializer(ModelSerializer):
    name = ReadOnlyField()
    class Meta:
        model = Profile
        fields = [
            'id',
            'name',
            'clan',
            'image',
            'location'
        ]

        def get_image(self,obj):
            try:
                image = obj.image.url 
            except:
                image = None
            return image
            
class ProfileListSerializer(ModelSerializer):
    name = ReadOnlyField()
    class Meta:
        model = Profile
        fields = [
            'name'
            'clan',
            'image'
        ]

        def get_image(self, obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image

