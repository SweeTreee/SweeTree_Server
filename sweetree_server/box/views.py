from rest_framework import (
    viewsets,
    mixins,
    status,
)

from .serializers import (
    BoxCreateSerializer,
    BoxRetrieveSerializer,
    BoxUpdateSerializer,
)

from box.models import Box

'''유저 인증 구현 뒤, 지울 것'''
from accounts.models import User


class BoxViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Box.objects.all()

    '''유저 인증 구현 뒤, 수정할 것'''
    def perform_create(self, serializer):
        serializer.save(user_id=User.objects.get(pk=1))
        # serializer.save(user_id=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return BoxCreateSerializer
        elif self.action == 'retrieve':
            return BoxRetrieveSerializer
        else:
            return BoxUpdateSerializer
