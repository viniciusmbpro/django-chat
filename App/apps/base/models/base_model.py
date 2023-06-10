from apps.base.models.mixins import BaseModelMixin
from apps.base.querysets import BaseQuerySet


class BaseModel(BaseModelMixin):
    objects = BaseQuerySet.as_manager()

    class Meta:
        abstract = True
