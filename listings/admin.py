from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pincode', 'seller', 'is_active', 'created_at')
    list_filter = ('category', 'pincode', 'is_active')
    search_fields = ('title', 'description', 'seller__full_name')
