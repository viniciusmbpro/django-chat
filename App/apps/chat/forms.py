from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Chat, Message

class ChatForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}),
        required=False
    )

    class Meta:
        model = Chat
        fields = ['name']
        labels = {'name': _('Nome')}

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participants'].queryset = user.friends.all()
        self.user = user

    def save(self, commit=True):
        chat = super().save(commit=False)
        chat.save()
        chat.participants.add(self.user)
        participants = self.cleaned_data['participants']
        if participants:
            chat.participants.add(*participants)
        return chat

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {'text': forms.TextInput(attrs={'placeholder': _('Digite a mensagem aqui...')})}
        labels = {'text': False}
