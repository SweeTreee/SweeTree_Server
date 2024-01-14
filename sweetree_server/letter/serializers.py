from rest_framework import serializers

from letter.models import Letter


class LetterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = [
            'nickname',
            'contents',
            'choco_type',
        ]


class LetterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = [
            'pk',
            'nickname',
            'contents',
            'choco_type',
            'created_at',
        ]
