from orders.models import Order
from rest_framework import viewsets
from orders.serializers import OrderSerializer
from rest_framework import viewsets


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer