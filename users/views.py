from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import (
    RegisterSerializer,
    CustomUserSerializer,
)
from rest_framework import status
from django.contrib.auth import login, logout
from guest_user.decorators import allow_guest_user


class CustomUserView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = get_object_or_404(CustomUser, pk=pk)
        user.delete()
        return Response({"message": "erfolgreich gelöscht"})


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]

        user = CustomUser.objects.get(username=username)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "user_id": user.pk,
                    "email": user.email,
                    "username": user.username,
                }
            )
        else:
            return Response({"error": "Falsche Anmeldedaten"}, status=400)


class GuestLoginView(APIView):
    @allow_guest_user
    def guest_view(self, request, *args, **kwargs):
        assert request.user.is_authenticated


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=204)


class RegisterUserView(APIView):
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
