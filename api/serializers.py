from rest_framework import serializers
from .models import User_details


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_details
        fields = ['token','user_name']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_details
        fields = '__all__'
        

