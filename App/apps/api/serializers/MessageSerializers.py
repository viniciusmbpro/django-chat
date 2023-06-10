from rest_framework import serializers

from apps.chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id', 'text',
            'chat', 'terms', 'video_paths',
            'created_at', 'modified_at', 'created_by',
        ]
