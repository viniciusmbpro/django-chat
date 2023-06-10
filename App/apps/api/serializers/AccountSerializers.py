from rest_framework import serializers

from apps.account.models import Account
from .ChatSerializers import ChatParticipantSerializer


class AccountBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 'email', 'username',
            'first_name', 'last_name', 'password',
        ]


class AccountAnonymousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 'email', 'username', 'first_name',
        ]


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 'email',
            'username', 'first_name', 'last_name',
            'created_at', 'modified_at', 'last_login',
            'photo'
        ]


class AccountMyChatsSerializer(serializers.ModelSerializer):
    my_chats = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = [
            'id', 'email', 'username',
            'my_chats',
        ]

    def get_my_chats(self, obj):
        return ChatParticipantSerializer(obj.chat_participants.filter(chat__created_by=obj), many=True).data  # noqa


class AccountParticipantChatsSerializer(serializers.ModelSerializer):  # noqa
    chat_participants = ChatParticipantSerializer(many=True)

    class Meta:
        model = Account
        fields = [
            'id', 'email', 'username',
            'chat_participants',
        ]
