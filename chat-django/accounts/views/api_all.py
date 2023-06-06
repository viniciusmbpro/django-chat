from accounts.forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chat.models import Chat
from chat.serializers import ChatSerializer


@api_view(['POST'])
def api_register_create(request):
    if not request.data:
        raise Http404()

    form = RegisterForm(request.data)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get('password', ''))
        user.save()

        messages.success(request, 'Your account was created successfully.')
        return Response(status=status.HTTP_201_CREATED)
    else:
        messages.error(request, 'Invalid form data')

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_login_create(request):
    if not request.data:
        raise Http404()

    print(request.data)
    form = LoginForm(request.data)

    if form.is_valid():
        user = authenticate(
            request,
            email=form.cleaned_data.get('email', ''),
            password=form.cleaned_data.get('password', '')
        )

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return Response(status=status.HTTP_200_OK)
        else:
            messages.error(request, 'Invalid email or password')
    else:
        messages.error(request, 'Invalid form data')

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@login_required(login_url='accounts:login', redirect_field_name='next')
def api_logout_view(request):
    if not request.data:
        messages.error(request, 'Invalid logout request')
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.data.get('username') != request.user.username:
        messages.error(request, 'Invalid logout user')
        return Response(status=status.HTTP_400_BAD_REQUEST)

    messages.success(request, 'Logged out successfully')
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@login_required(login_url='accounts:login', redirect_field_name='next')
def api_dashboard(request):
    chats = Chat.objects.filter(chat_participants__user=request.user)
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)
