from django.db.models import Prefetch
from django.db.models import Q
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.chat.models import Chat, ChatParticipant, Message


class ChatListViewBase(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    # redirect_field_name = ''
    model = Chat
    context_object_name = 'chats'
    template_name = 'chat/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.annotate(
            is_participant=Count(
                'chat_participants',
                filter=Q(
                    chat_participants__user=self.request.user
                ),
                distinct=True),
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_title = _('Chats')

        ctx.update({
            'page_title': page_title,
            'additional_url_query': '',
        })

        return ctx


class ChatGetInView(LoginRequiredMixin, View):
    login_url = '/accounts/login'

    def post(self, request, id):
        chat = get_object_or_404(Chat, id=id)

        # Verifica se o usuário já é participante do chat
        if ChatParticipant.objects.filter(chat=chat, user=request.user).exists():  # noqa
            return render(
                request, 'chat/pages/chat-view.html',
                {
                    'chat': chat,
                    'error_message': 'Você já é participante deste chat.'
                })

        # Adiciona o usuário como participante do chat
        participant = ChatParticipant(chat=chat, user=request.user)
        participant.save()

        # Redireciona para a rota chat-view
        return redirect(reverse('chat:chat-view', kwargs={'id': chat.id}))


class ChatListViewSearch(ChatListViewBase):
    template_name = 'chat/pages/search.html'

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get('q', '')

        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            Q(name__icontains=search_term) |
            Q(chat_participants__user__email__icontains=search_term)
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q', '')

        ctx.update({
            'page_title': f'Search for "{search_term}" |',
            'search_term': search_term,
            'additional_url_query': f'&q={search_term}',
        })

        return ctx


class ChatDetail(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    pk_url_kwarg = 'id'

    model = Chat
    context_object_name = 'chat'
    template_name = 'chat/pages/chat-view.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.prefetch_related(
            Prefetch(
                'chat_participants',
                queryset=ChatParticipant.objects.select_related('user'),
            ),
            Prefetch(
                'messages_to',
                queryset=Message.objects.select_related('chat'),
            ),
        )

        return qs


class ChatAddMessageView(LoginRequiredMixin, View):
    login_url = '/accounts/login'

    def post(self, request, id):
        chat = get_object_or_404(Chat, id=id)

        # Verifica se o usuário é participante do chat
        if not ChatParticipant.objects.filter(chat=chat, user=request.user).exists():  # noqa
            return render(
                request, 'chat/pages/chat-view.html',
                {
                    'chat': chat,
                    'error_message': 'Você não é participante deste chat.'
                })

        # Adiciona a mensagem no chat
        message = Message(
            text=request.POST['message'],
            chat=chat,
            created_by=request.user,
            modified_by=request.user,
        )
        message.save()

        # Redireciona para a rota chat-view
        return redirect(reverse('chat:chat-view', kwargs={'id': chat.id}))
