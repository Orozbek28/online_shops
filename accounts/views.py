from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from .models import User
from .serializers import UserRegisterSerializer, UserSerializer
from .permissions import AuthTokenPermission


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer


class MyObtainAuthToken(ObtainAuthToken):
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [AuthTokenPermission]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)