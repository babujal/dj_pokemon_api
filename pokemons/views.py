from .models import Pokemon
from rest_framework import viewsets, permissions, status
from .serializers import PokemonSerializers, UserSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset=Pokemon.objects.all()
    # serializers_class=PokemonSerializers
    serializer_class=PokemonSerializers
    # permission_classes=[permissions.AllowAny]
    permission_classes=[IsAuthenticated]
    # automatically associate the pokemon with the authenticated user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # only return pokemon owned by the authenticated user
    def get_queryset(self):
        return Pokemon.objects.filter(user=self.request.user)
    
class UserRegistrationView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    