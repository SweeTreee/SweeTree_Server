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

from sweetree_server.box.models import Box


class BoxViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Box.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return BoxCreateSerializer
        elif self.action == 'retrieve':
            return BoxRetrieveSerializer
        else:
            return BoxUpdateSerializer
