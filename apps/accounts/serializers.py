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

from apps.accounts.models import Profile, Clan, ProfileImg

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

