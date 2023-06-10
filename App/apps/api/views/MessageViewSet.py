from rest_framework.permissions import IsAuthenticated  # noqa
from apps.api.permissions import IsOwner
from apps.chat.models import Message
from apps.api.serializers import (
    MessageSerializer,
)
from rest_framework import viewsets, mixins


class MessageViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]
        if self.action == 'create':
            self.permission_classes = []
        else:
            self.permission_classes.append(IsOwner)

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, modified_by=self.request.user)  # noqa

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)
