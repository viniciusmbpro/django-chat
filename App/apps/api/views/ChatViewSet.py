from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.api.permissions import IsOwner, IsParticipant
from rest_framework.response import Response
from apps.chat.models import Chat, ChatParticipant
from apps.account.models import Account
from drf_spectacular.utils import extend_schema, OpenApiExample
from apps.api.serializers import (
    ChatBaseSerializer,
    ChatSerializerAnonymous,
    ChatDetailSerializer,
    MessageSerializer,
)
from rest_framework import viewsets
from rest_framework.decorators import action


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]
        if self.action == 'retrieve':
            self.permission_classes.append(IsParticipant)
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':  # noqa
            self.permission_classes.append(IsOwner)

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'list':
            return ChatSerializerAnonymous
        elif self.action == 'retrieve':
            return ChatDetailSerializer
        elif self.action == 'add_message':
            return MessageSerializer
        else:
            return ChatBaseSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, modified_by=self.request.user)  # noqa

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

    @extend_schema(
        description="Add participant.",
        request=ChatBaseSerializer,
        responses={
            200: ChatBaseSerializer,
        },
        examples=[
            OpenApiExample(
                name="Example Request",
                value={
                    "id_account": "1",
                }
            ),
        ]
    )
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated],
        url_path='add-participant')
    def add_participant(self, request, pk):
        chat = get_object_or_404(Chat, id=pk)
        account = get_object_or_404(
            Account, id=request.data.get('id_account'))

        if not ChatParticipant.objects.filter(chat=chat, user=account).exists():  # noqa
            ChatParticipant.objects.create(chat=chat, user=account)
        else:
            return Response(
                {'detail': 'Este usuário já é participante deste chat.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {'detail': 'Participante adicionado com sucesso.'},
            status=status.HTTP_200_OK
        )

    @extend_schema(
        description="Remove participant.",
        request=ChatBaseSerializer,
        responses={
            200: ChatBaseSerializer,
        },
        examples=[
            OpenApiExample(
                name="Example Request",
                value={
                    "id_account": "1",
                }
            ),
        ]
    )
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated],
        url_path='remove-participant')  # noqa
    def remove_participant(self, request, pk):
        chat = get_object_or_404(Chat, id=pk)
        account = get_object_or_404(
            Account, id=request.data.get('id_account'))

        if ChatParticipant.objects.filter(chat=chat, user=account).exists():
            ChatParticipant.objects.filter(chat=chat, user=account).delete()
        else:
            return Response(
                {'detail': 'Este usuário não é participante deste chat.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {'detail': 'Usuário removido do chat com sucesso.'},
            status=status.HTTP_200_OK
        )

    @extend_schema(
        description="Add message.",
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
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated, IsParticipant],
        url_path='add-message')  # noqa
    def add_message(self, request, pk):
        chat = get_object_or_404(Chat, id=pk)
        serializer = MessageSerializer(data=request.data)

        serializer.initial_data['chat'] = chat.id

        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user, modified_by=self.request.user, chat=chat)  # noqa

        return Response(
            {'detail': 'Mensagem adicionada com sucesso.'},
            status=status.HTTP_200_OK
        )
