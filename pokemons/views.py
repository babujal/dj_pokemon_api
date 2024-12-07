from .models import Pokemon
from rest_framework import viewsets, permissions
from .serializers import PokemonSerializer

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    #Everything in the Pokemon object (which is everything -everything)
    queryset=Pokemon.objects.all()
    # sepcificies the which serializer to use. In this case, we will be use the file: PokemonSerializer to do the serialization and deserialization
    serializer_class=PokemonSerializer
    # unrestricted access to the api
    permission_classes=[permissions.AllowAny]