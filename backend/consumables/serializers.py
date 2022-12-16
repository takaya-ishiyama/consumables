from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Items
from accounts.serializers import UserSerializer

class ItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Items
        fields = (
            'user',
            'id',
            'name',
            'image',
            'status',
            'text',
            'created_at'
        )
        