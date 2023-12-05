from users.models import User
from rest_framework import viewsets
from users.serializers import UserSerializer
from rest_framework import viewsets
from .per import UserPermission

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]