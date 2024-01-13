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


class LetterViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):

    @action(detail=False, methods=['get'])
    def count(self, request, *args, **kwargs):
        return Response({'count': self.get_queryset().count()})

    def get_serializer_class(self):
        if self.action == 'create':
            return LetterCreateSerializer
        elif self.action == 'list':
            return LetterListSerializer

    def get_queryset(self):
        return Letter.objects.filter(box_id=self.kwargs.get('box_id'))

    '''NEED TO FIX'''
    # def get_permissions(self):
    #     if self.action == 'create':
    #         return [IsAuthenticated()]
    #     elif self.action == 'list':
    #         return [AllowAny()]
    #     else:
    #         return super().get_permissions()
