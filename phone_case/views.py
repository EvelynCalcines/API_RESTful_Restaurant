# Django and DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# waning_moon_design imports
from .serializers import PhoneCaseSerializer
from phone_case.models import PhoneCase


class PhoneCaseViewSet(GenericViewSet):

    queryset = PhoneCase.objects.all()
    serializer_class = PhoneCaseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
