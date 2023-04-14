from core.base.models.mixins import BaseModelMixin
from core.base.querysets import BaseQuerySet

class BaseModel(BaseModelMixin):
    objects = BaseQuerySet.as_manager()

    class Meta:
        abstract = True