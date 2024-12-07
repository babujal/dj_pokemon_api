from .models import Pokemon
from rest_framework import serializers

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model=Pokemon
            fields='__all__'