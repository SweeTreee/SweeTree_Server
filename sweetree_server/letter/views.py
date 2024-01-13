from rest_framework import (
    viewsets,
    mixins,
    status,
)

from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)

from .serializers import (
    LetterCreateSerializer,
    LetterListSerializer,
)

from letter.models import Letter
from box.models import Box


class LetterViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):

    def perform_create(self, serializer):
        box = Box.objects.get(pk=self.kwargs.get('box_pk'))
        serializer.save(box_id=box)

    @action(detail=False, methods=['get'])
    def count(self, request, *args, **kwargs):
        return Response({'count': self.get_queryset().count()})

    def get_serializer_class(self):
        if self.action == 'create':
            return LetterCreateSerializer
        elif self.action == 'list':
            return LetterListSerializer

    def get_queryset(self):
        box = Box.objects.get(pk=self.kwargs.get('box_pk'))
        return Letter.objects.filter(box_id=box)

    '''NEED TO FIX'''
    # def get_permissions(self):
    #     if self.action == 'create':
    #         return [IsAuthenticated()]
    #     elif self.action == 'list':
    #         return [AllowAny()]
    #     else:
    #         return super().get_permissions()
