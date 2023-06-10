# from apps.account.forms.chat_form import AccountChatForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from apps.chat.models import Chat
from apps.account.forms.chat_form import AccountChatForm


@login_required(login_url='accounts:login', redirect_field_name='next')
def dashboard(request):
    chats = Chat.objects.filter(
        chat_participants__user=request.user, created_by=request.user)
    return render(
        request,
        'accounts/pages/dashboard.html',
        context={
            'chats': chats,
        }
    )


@method_decorator(
    login_required(login_url='accounts:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardChat(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_chat(self, id=None):
        chat = None

        if id is not None:
            chat = Chat.objects.filter(id=id).first()

            if not chat:
                raise Http404()

        return chat

    def render_chat(self, form):
        return render(
            self.request,
            'accounts/pages/dashboard_chat.html',
            context={
                'form': form
            }
        )

    def get(self, request, id=None):
        chat = self.get_chat(id)
        form = AccountChatForm(instance=chat)
        return self.render_chat(form)

    def post(self, request, id=None):
        chat = self.get_chat(id)
        form = AccountChatForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=chat
        )

        if form.is_valid():
            # Agora, o form é válido e eu posso tentar salvar
            chat = form.save(commit=False)

            chat.created_by = request.user
            chat.modified_by = request.user

            chat.save()

            messages.success(request, 'Seu chat foi criado com sucesso!')
            return redirect(
                reverse('chat:dashboard')
            )

        return self.render_chat(form)


@method_decorator(
    login_required(login_url='accounts:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardChatDelete(DashboardChat):
    def post(self, *args, **kwargs):
        chat = self.get_chat(self.request.POST.get('id'))

        # verifica se o usuário é o criador do chat
        if chat.created_by != self.request.user:
            messages.error(
                self.request, 'You are not the creator of this chat.')
            return redirect(reverse('chat:dashboard'))

        chat.delete()
        messages.success(self.request, 'Deleted successfully.')
        return redirect(reverse('chat:dashboard'))
