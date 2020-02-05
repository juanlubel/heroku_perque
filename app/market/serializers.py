from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'slug',
            'owner',
            'name',
            'quality',
            'buy_price',
            'sell_price'
        ]
        read_only_fields = ['owner']

    def validate_slug(self, value):
        queryset = Item.objects.filter(slug__iexact=value)
        if self.instance:
            queryset = queryset.exclude(slug=self.instance.slug)
        if queryset.exists():
            raise serializers.ValidationError("This slug is already be in use")
        return value

