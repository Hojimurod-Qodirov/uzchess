from rest_framework import serializers
from .models import PurchasedItem

class PurchasedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedItem
        fields = ('id', 'item_name', 'item_type', 'price', 'purchased_at')