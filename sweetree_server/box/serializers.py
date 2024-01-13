from rest_framework import serializers

from box.models import Box


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
            '''유저 인증 구현 뒤, 수정할 것'''
            # 'user_id',
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
