from rest_framework import serializers

from sweetree_server.box.models import Box


class BoxRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = [
            'pk',
            'box_name',
            'box_type',
            'is_box_public',
            'created_at',
        ]


class BoxCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = [
            'user_id',
            'box_name',
            'box_type',
            'is_box_public',
        ]


class BoxUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = [
            'box_name',
            'box_type',
            'is_box_public',
        ]