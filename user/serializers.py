from rest_framework import serializers
from .models import CustomUser, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_picture')

class UserDetailSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'profile')