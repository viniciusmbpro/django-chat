from rest_framework import serializers
from .models import Chat, ChatParticipant, Message
from accounts.serializers import AccountSerializer


class ChatParticipantSerializer(serializers.ModelSerializer):
    user = AccountSerializer()

    class Meta:
        model = ChatParticipant
        fields = ('id', 'user')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'text', 'chat', 'terms',
                  'video_paths', 'created_at')


class ChatSerializer(serializers.ModelSerializer):
    chat_participants = ChatParticipantSerializer(many=True, read_only=True)
    messages_to = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ('id', 'name', 'chat_participants',
                  'messages_to', 'created_at')
