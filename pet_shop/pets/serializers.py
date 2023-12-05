from rest_framework import serializers
from pets.models import Pet


class PetSerializer(serializers.HyperlinkedModelSerializer):
    # pet = serializers.HyperlinkedRelatedField(many=True, view_name='pet-detail', read_only=True)

    class Meta:
        model = Pet
        fields = ['url','petid','name','price','title']

