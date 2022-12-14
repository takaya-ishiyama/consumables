from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Items

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id','name','image','status' ,'text' ,'created_at')
        