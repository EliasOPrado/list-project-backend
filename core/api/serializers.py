from rest_framework import serializers
from ..models import Item, List


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many=True)

    class Meta:
        model = List
        fields = ['id', 'name', 'owner', 'url', 'item_set']
