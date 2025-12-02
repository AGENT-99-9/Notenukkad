from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.full_name', read_only=True)
    seller_phone = serializers.CharField(source='seller.phone', read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'category',
            'price',
            'city',
            'pincode',
            'seller',
            'seller_name',
            'seller_phone',
            'created_at',
            'is_active',
        ]
        read_only_fields = ['seller', 'created_at', 'seller_name', 'seller_phone']

    def create(self, validated_data):
        """
        Set seller = logged-in user.
        Copy city & pincode from user if not explicitly provided.
        """
        request = self.context.get('request')
        user = request.user

        # Default: use user city/pincode if not in request
        if 'city' not in validated_data:
            validated_data['city'] = user.city
        if 'pincode' not in validated_data:
            validated_data['pincode'] = user.pincode

        validated_data['seller'] = user
        return super().create(validated_data)
