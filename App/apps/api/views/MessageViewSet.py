from rest_framework.permissions import IsAuthenticated  # noqa
from apps.api.permissions import IsOwner
from apps.chat.models import Message
from apps.api.serializers import (
    MessageSerializer,
)
from rest_framework import viewsets, mixins
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter, OpenApiTypes  # noqa


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

    @extend_schema(
        description="Update message.",
        request=MessageSerializer,
        responses={
            200: MessageSerializer,
        },
        examples=[
            OpenApiExample(
                name="Example Request",
                value={
                    "text": "string",
                    "terms": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    },
                    "video_paths": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    },
                }
            ),
        ]
    )
    def update(self, request, *args, **kwargs):
        request.data['chat'] = Message.objects.get(id=kwargs['pk']).chat.id.__str__()  # noqa
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description="Update message.",
        request=MessageSerializer,
        responses={
            200: MessageSerializer,
        },
        examples=[
            OpenApiExample(
                name="Example Request",
                value={
                    "text": "string",
                    "terms": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    },
                    "video_paths": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    },
                }
            ),
        ]
    )
    def partial_update(self, request, *args, **kwargs):
        request.data['chat'] = Message.objects.get(id=kwargs['pk']).chat.id.__str__()  # noqa
        return super().partial_update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, modified_by=self.request.user)  # noqa

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)
