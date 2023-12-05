from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # pet = serializers.HyperlinkedRelatedField(many=True, view_name='pet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url','userid','fullname','email','age']

