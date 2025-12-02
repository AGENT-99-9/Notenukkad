from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

from listings.serializers import ListingSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'phone', 'city', 'pincode', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class FavoriteListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'favorites']
        depth = 1
