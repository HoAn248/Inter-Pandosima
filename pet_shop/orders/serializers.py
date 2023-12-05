from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    # pet = serializers.HyperlinkedRelatedField(many=True, view_name='pet-detail', read_only=True)

    class Meta:
        model = Order
        fields = ['orderid','userid','petid','des']

