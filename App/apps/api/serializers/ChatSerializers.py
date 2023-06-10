from rest_framework import serializers

from apps.chat.models import Chat, ChatParticipant
from .MessageSerializers import MessageSerializer


class ChatParticipantSerializer(serializers.ModelSerializer):
    chat_name = serializers.ReadOnlyField(source='chat.name')
    chat_id = serializers.ReadOnlyField(source='chat.id')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = ChatParticipant
        fields = [
            'id', 'chat_id', 'user_id',
            'chat_name'
        ]


class ChatBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'id', 'name',
            'description',
        ]


class ChatDetailSerializer(serializers.ModelSerializer):
    participants_count = serializers.SerializerMethodField()
    messages_count = serializers.SerializerMethodField()
    chat_participants = ChatParticipantSerializer(many=True)
    messages_to = MessageSerializer(many=True)
    owner = serializers.ReadOnlyField(source='created_by.email')

    class Meta:
        model = Chat
        fields = [
            'id', 'name',
            'description', 'owner', 'created_at',
            'modified_at', 'participants_count', 'messages_count',
            'chat_participants', 'messages_to',
        ]

    def get_participants_count(self, obj):
        return obj.participants_count

    def get_messages_count(self, obj):
        return obj.messages_count


class ChatSerializerAnonymous(serializers.ModelSerializer):
    participants_count = serializers.SerializerMethodField()
    messages_count = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = [
            'id', 'name', 'description',
            'participants_count', 'messages_count',
        ]

    def get_participants_count(self, obj):
        return obj.participants_count

    def get_messages_count(self, obj):
        return obj.messages_count
