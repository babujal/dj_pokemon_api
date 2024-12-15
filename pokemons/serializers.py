from .models import Pokemon
from rest_framework import serializers
from django.contrib.auth.models import User

class PokemonSerializers(serializers.HyperlinkedModelSerializer):
    user=serializers.ReadOnlyField(source='user.username') #Every pokemon will have a user field based on the UserZerializer below
    class Meta:
            model=Pokemon
            fields='__all__'

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username', 'email', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

            
            