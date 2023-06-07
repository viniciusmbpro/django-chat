from accounts.forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from chat.models import Chat
from chat.serializers import ChatSerializerAuthenticated
from rest_framework.views import APIView
from accounts.serializers import AccountSerializer


class ApiRegisterCreateView(APIView):
    serializer_class = AccountSerializer

    def post(self, request):
        if not request.data:
            raise Http404()

        form = RegisterForm(request.data)
        form.data['password2'] = form.data['password']

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password', ''))
            user.save()

            messages.success(request, 'Your account was created successfully.')
            return Response(status=status.HTTP_201_CREATED)
        else:
            messages.error(request, 'Invalid form data')

        return Response(status=status.HTTP_400_BAD_REQUEST)


class ApiDashboardView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatSerializerAuthenticated

    def get(self, request):
        chats = Chat.objects.filter(chat_participants__user=request.user)
        serializer = ChatSerializerAuthenticated(chats, many=True)
        return Response(serializer.data)
