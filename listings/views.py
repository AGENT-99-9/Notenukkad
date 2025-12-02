from rest_framework import generics, permissions
from .models import Listing
from .serializers import ListingSerializer
from .permissions import IsOwnerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class ListingListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/listings/        -> List listings (with filters) [CACHED]
    POST /api/listings/        -> Create listing (auth required)
    """
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Listing.objects.filter(is_active=True).select_related('seller')

        category = self.request.query_params.get('category')
        pincode = self.request.query_params.get('pincode')
        city = self.request.query_params.get('city')
        search = self.request.query_params.get('search')

        if category:
            queryset = queryset.filter(category=category.upper())
        if pincode:
            queryset = queryset.filter(pincode=pincode)
        if city:
            queryset = queryset.filter(city__iexact=city)
        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset

    @method_decorator(cache_page(60 * 5))  # 5 minutes cache
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()



class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/listings/<id>/  -> Public detail
    PUT    /api/listings/<id>/  -> Update (only seller)
    PATCH  /api/listings/<id>/  -> Partial update
    DELETE /api/listings/<id>/  -> Soft delete (we’ll do hard delete for now)
    """
    queryset = Listing.objects.select_related('seller')
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
