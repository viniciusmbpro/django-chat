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


class ChatSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'name')
    

class ChatSerializerAnonymous(serializers.ModelSerializer):
    participants_count = serializers.SerializerMethodField()
    messages_count = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ('id', 'name', 'participants_count', 'messages_count')

    def get_participants_count(self, obj):
        return obj.participants_count
    
    def get_messages_count(self, obj):
        return obj.messages_count


class ChatSerializerAuthenticated(serializers.ModelSerializer):
    participants_count = serializers.SerializerMethodField()
    messages_count = serializers.SerializerMethodField()
    chat_participants = ChatParticipantSerializer(many=True)
    messages_to = MessageSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'name', 'participants_count', 'messages_count', 'chat_participants', 'messages_to')

    def get_participants_count(self, obj):
        return obj.participants_count
    
    def get_messages_count(self, obj):
        return obj.messages_count
