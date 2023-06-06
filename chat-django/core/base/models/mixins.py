import uuid

from django.db.models import Model
from django.db.models.fields import UUIDField, DateTimeField
from django.db.models.fields.related import ForeignKey, CASCADE


class BaseModelMixin(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="id", db_index=True, help_text="Identificador único do registro")  # noqa
    created_by = ForeignKey(
        to="accounts.Account",
        verbose_name="criado por",
        on_delete=CASCADE,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
    )
    modified_by = ForeignKey(
        to="accounts.Account",
        verbose_name="modificado por",
        on_delete=CASCADE,
        related_name="%(class)s_modified_by",
        null=True,
        blank=True,
    )
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
