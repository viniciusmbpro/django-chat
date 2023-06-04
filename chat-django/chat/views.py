"""
Módulo de Views do aplicativo 'chat'

Este arquivo contém as definições das views responsáveis por lidar com as requisições feitas às diferentes URLs do aplicativo 'chat'. Essas views fornecem a lógica para manipular as solicitações e interagir com o modelo de dados subjacente para realizar as operações desejadas nos chats e em suas mensagens.

As seguintes URLs estão definidas neste arquivo:

1. 'chat-list': Exibe uma lista de chats.
2. 'chat-detail': Mostra os detalhes de um chat específico.
3. 'chat-delete': Exclui um chat.
4. 'chat-update': Atualiza os detalhes de um chat.
5. 'chat-archive': Arquiva um chat.
6. 'chat-unarchive': Desarquiva um chat.
7. 'chat-trash': Move um chat para a lixeira.
8. 'chat-restore': Restaura um chat da lixeira.

Além disso, existem várias outras URLs relacionadas a operações nas mensagens de um chat, incluindo visualização, exclusão, atualização, resposta, encaminhamento, arquivamento, desarquivamento, movimento para lixeira, entre outras.

Cada view é implementada como uma função ou classe baseada em vista, fornecendo a lógica necessária para responder às requisições HTTP correspondentes. As views interagem com o modelo de dados do aplicativo 'chat' para realizar as operações solicitadas, como recuperar informações, criar, atualizar ou excluir registros de chat e mensagens.

Para cada URL, é fornecido um nome para facilitar a referência e o redirecionamento correto dentro do aplicativo.

"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView, FormView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormMixin

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the chat index.")
