from pets.models import Pet
from rest_framework import viewsets
from pets.serializers import PetSerializer
from rest_framework import viewsets


class PetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer