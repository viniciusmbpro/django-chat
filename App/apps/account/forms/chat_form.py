from collections import defaultdict
from django import forms
from django.core.exceptions import ValidationError
from apps.chat.models import Chat
from apps.account.validators import AccountChatValidator


class AccountChatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._my_errors = defaultdict(list)

    class Meta:
        model = Chat
        fields = ['name']

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        validator = AccountChatValidator(
            self.cleaned_data, ErrorClass=ValidationError)
        try:
            validator.clean()
        except ValidationError as e:
            self.add_error(None, e)
        return super_clean
