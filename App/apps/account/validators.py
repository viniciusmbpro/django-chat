from collections import defaultdict
from django.core.exceptions import ValidationError


class AccountChatValidator:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = defaultdict(list) if errors is None else errors
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean()

    def clean(self, *args, **kwargs):
        self.clean_name()
        # self.clean_chat_participants()

        # cd = self.data

        # name = cd.get('name')

        # Validações adicionanis aqui
        # ...

        if self.errors:
            raise self.ErrorClass(self.errors)

    def clean_name(self):
        name = self.data.get('name')

        if len(name) < 5:
            self.errors['name'].append('Must have at least 5 chars.')

        return name
