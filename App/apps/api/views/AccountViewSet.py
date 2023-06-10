from rest_framework.permissions import IsAuthenticated  # noqa
from apps.api.permissions import IsOwnerAccount
from apps.account.models import Account
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter, OpenApiTypes  # noqa
from apps.api.serializers import (
    AccountBaseSerializer,
    AccountAnonymousSerializer,
    AccountDetailSerializer,
    AccountMyChatsSerializer,
    AccountParticipantChatsSerializer,
)
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action
from django.db.models import Q


class AccountViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    queryset = Account.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, IsOwnerAccount]
        if self.action == 'create' or self.action == 'search':
            self.permission_classes = []

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AccountDetailSerializer
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'create':  # noqa
            return AccountBaseSerializer
        else:
            return AccountAnonymousSerializer

    @extend_schema(
        description="Create account.",
        request=AccountBaseSerializer,
        responses={
            200: AccountBaseSerializer,
        },
        examples=[
            OpenApiExample(
                name="Example Request",
                value={
                    "email": "email@example.com",
                    "username": "myusername",
                    "first_name": "My first name",
                    "last_name": "My last name",
                    "password": "MyPassword123",
                }
            ),
        ]
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data.get('password')
        account = Account.objects.create(**serializer.validated_data)
        account.set_password(password)
        account.save()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers)

    @extend_schema(
        description="Search account by email and/or username.",
        request=None,
        parameters=[
            OpenApiParameter(
                    name='q',
                    description='Search query parameter (email or username)',
                    required=False,
                    type=OpenApiTypes.STR
            ),
        ],
        responses={
            200: AccountBaseSerializer(many=True),
        },
        examples=[
            OpenApiExample(
                name="Example Request",
                value="/api/accounts/search/?q=email@example.com"
            ),
        ]
    )
    @action(
        detail=False, methods=['get'],
        permission_classes=[IsAuthenticated],
        url_path='search')
    def search(self, request):
        q = request.query_params.get('q')

        if q:
            queryset = Account.objects.filter(
                Q(email__icontains=q) | Q(username__icontains=q)
            )
        else:
            queryset = Account.objects.none()

        serializer = AccountAnonymousSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated], url_path='me')  # noqa
    def me(self, request):
        serializer = AccountDetailSerializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated], url_path='my-chats')  # noqa
    def my_chats(self, request):
        serializer = AccountMyChatsSerializer(request.user, context={'request': request})  # noqa
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated], url_path='participant-chats')  # noqa
    def participant_chats(self, request):
        serializer = AccountParticipantChatsSerializer(
            request.user, context={'request': request})
        return Response(serializer.data)
