from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from listings.serializers import ListingSerializer
from listings.models import Listing


from rest_framework import serializers

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user



class FavoriteListView(generics.ListAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.favorites.all()


class ToggleFavoriteView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Listing.objects.all()  # dummy queryset for Swagger

    class DummySerializer(serializers.Serializer):
        message = serializers.CharField()
    serializer_class = DummySerializer

    def post(self, request, pk):
        listing = Listing.objects.get(pk=pk)
        user = request.user
        user.favorites.add(listing)
        return Response({"message": "Added to favorites"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        listing = Listing.objects.get(pk=pk)
        user = request.user
        user.favorites.remove(listing)
        return Response({"message": "Removed from favorites"}, status=status.HTTP_200_OK)

