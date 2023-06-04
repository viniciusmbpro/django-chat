# abaixo segue o arquivo de serializers
#
from rest_framework import serializers
from .models import Message
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.models import Count
from django.db.models import Case, When
from django.db.models import Value
from django.db.models import BooleanField
from django.db.models import Subquery
from django.db.models import OuterRef
from django.db.models import Exists
from django.db.models import F
from django.db.models import IntegerField
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Max
from django.db.models import Min
from django.db.models import Func
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateTimeField
from django.db.models import DateField
from django.db.models import DurationField
from django.db.models import DecimalField
from django.db.models import FloatField
from django.db.models import ExpressionWrapper

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
        }
    
    def to_internal_value(self, data):
        return {
            'id': data.get('id'),
            'username': data.get('username'),
        }

    
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'created_at']
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'sender': UserSerializer(instance.sender).data,
            'recipient': UserSerializer(instance.recipient).data,
            'content': instance.content,
            'created_at': instance.created_at,
        }
    
    def to_internal_value(self, data):
        return {
            'id': data.get('id'),
            'sender': data.get('sender'),
            'recipient': data.get('recipient'),
            'content': data.get('content'),
            'created_at': data.get('created_at'),
        }


class MessageSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'created_at']
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'sender': UserSerializer(instance.sender).data,
            'recipient': UserSerializer(instance.recipient).data,
            'content': instance.content,
            'created_at': instance.created_at,
        }
    
    def to_internal_value(self, data):
        return {
            'id': data.get('id'),
            'sender': data.get('sender'),
            'recipient': data.get('recipient'),
            'content': data.get('content'),
            'created_at': data.get('created_at'),
        }


class MessageSerializerV3(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'created_at']
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'sender': UserSerializer(instance.sender).data,
            'recipient': UserSerializer(instance.recipient).data,
            'content': instance.content,
            'created_at': instance.created_at,
        }
    
    def to_internal_value(self, data):
        return {
            'id': data.get('id'),
            'sender': data.get('sender'),
            'recipient': data.get('recipient'),
            'content': data.get('content'),
            'created_at': data.get('created_at'),
        }