from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q
from django.db.models.aggregates import Count
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from chat.models import Chat, ChatParticipant, Message
from chat.serializers import (
    ChatSerializer, ChatParticipantSerializer, MessageSerializer
)


class ChatOperationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Chat.objects.annotate(
            participants_count=Count('chat_participants'),
            messages_count=Count('messages_to'),
            is_participant=Count('chat_participants', filter=Q(
                chat_participants__user=self.request.user)),
        )
        serializer = ChatSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        chat = get_object_or_404(Chat, id=id)
        serializer = ChatSerializer(chat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        chat = get_object_or_404(Chat, id=id)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChatDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        chat = get_object_or_404(Chat, id=id)
        serializer = ChatSerializer(chat)
        return Response(serializer.data)


class ChatAddParticipantAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        chat = get_object_or_404(Chat, id=id)

        if ChatParticipant.objects.filter(chat=chat, user=request.user).exists():
            return Response(
                {'detail': 'Você já é participante deste chat.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        participant = ChatParticipant(chat=chat, user=request.user)
        participant.save()

        return Response(status=status.HTTP_201_CREATED)


class ChatAddMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        chat = get_object_or_404(Chat, id=id)

        if not ChatParticipant.objects.filter(chat=chat, user=request.user).exists():
            return Response(
                {'detail': 'Você não é participante deste chat.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        message = Message(
            text=request.data['message'],
            chat=chat,
            created_by=request.user,
            modified_by=request.user,
        )
        message.save()

        return Response(status=status.HTTP_201_CREATED)
