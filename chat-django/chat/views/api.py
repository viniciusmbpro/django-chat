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
    ChatSerializerAnonymous, ChatParticipantSerializer, MessageSerializer, ChatSerializerAuthenticated
)
from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes
from accounts.forms.chat_form import AccountChatForm


class ChatListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatSerializerAnonymous

    def get(self, request):
        qs = Chat.objects.all()
        serializer = ChatSerializerAnonymous(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ChatSerializerAuthenticated(data=request.data)
        if serializer.is_valid():
            
            serializer.validated_data['created_by'] = request.user
            serializer.validated_data['modified_by'] = request.user

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatDeleteUpdateAPIView(APIView):
    serializer_class = ChatSerializerAuthenticated
    # http_method_names = ['delete','put', 'get', 'head', 'options',]

    def delete(self, request, id):
        chat = get_object_or_404(Chat, id=id)
        # verificar se o usuário é o criador do chat
        if chat.created_by != request.user:
            return Response(
                {'detail': 'Você não tem permissão para excluir este chat.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        chat = get_object_or_404(Chat, id=id)
        serializer = ChatSerializerAuthenticated(chat, data=request.data)

        # verificar se o usuário é o criador do chat
        if chat.created_by != request.user:
            return Response(
                {'detail': 'Você não tem permissão para editar este chat.'},
                status=status.HTTP_403_FORBIDDEN
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id):
        chat = get_object_or_404(Chat, id=id)
        serializer = ChatSerializerAuthenticated(chat)

        # verificar se o usuário é participante do chat
        if not ChatParticipant.objects.filter(chat=chat, user=request.user).exists():
            return Response(
                {'detail': 'Você não é participante deste chat.'},
                status=status.HTTP_403_FORBIDDEN
            )

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
