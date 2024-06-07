from rest_framework import serializers

from .models import *


class MarketDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MarketDetail
        fields = '__all__'