import logging

from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.serializers import EmailTokenObtainPairSerializer, RegisterSerializer

logger = logging.getLogger(__name__)


class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = EmailTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        email = request.data.get("email", "")
        client_ip = (request.META.get("HTTP_X_FORWARDED_FOR") or request.META.get("REMOTE_ADDR", "")).split(",")[0].strip()

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            logger.warning("Login failed for email=%s ip=%s.", email, client_ip)
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.user
        logger.info("Login success for email=%s ip=%s", user.email, client_ip)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RefreshAccessTokenView(TokenRefreshView):
    permission_classes = [AllowAny]


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.save()
        tokens['email'] = serializer.validated_data['email']

        return Response(tokens, status=status.HTTP_201_CREATED)
