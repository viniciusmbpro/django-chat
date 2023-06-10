from rest_framework import permissions
from apps.chat.models import ChatParticipant


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class IsParticipant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return ChatParticipant.objects.filter(chat=obj, user=request.user).exists()  # noqa


class IsOwnerAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
