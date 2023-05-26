# Django and DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import mixins, GenericViewSet

# waning_moon_design imports
from .models import User
from .serializers import (RegistrationSerializer, UserSerializer, LoginSerializer)


class RegisterViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):  # login
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
