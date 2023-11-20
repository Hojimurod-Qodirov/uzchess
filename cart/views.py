from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import PurchasedItem
from .serializers import PurchasedItemSerializer

class ShoppingCartAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        purchased_items = PurchasedItem.objects.filter(user=request.user)
        serializer = PurchasedItemSerializer(purchased_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchasedItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)