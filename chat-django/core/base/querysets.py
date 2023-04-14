from django.db import models
from django.db.models.query import QuerySet


class BaseQuerySet(QuerySet):
    pass

class MessageQuerySet(BaseQuerySet):
    def messages_between_users(self, user1, user2):
        return self.filter(sender__in=[user1, user2], recipient__in=[user1, user2]).order_by("-created_at")
